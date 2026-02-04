#!/usr/bin/env python3
"""
Update updated_at field in Jekyll posts based on Git last commit date.
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

def get_git_last_modified(file_path):
    """Get the last commit date for a file from git."""
    try:
        # Use repository root as cwd so git paths resolve correctly
        repo_root = Path(__file__).resolve().parents[1]

        # Iterate commits for the file and pick the most recent commit
        # that includes a meaningful change (i.e. not only changes to the
        # `updated_at` frontmatter line introduced by this script).
        commits = subprocess.run(
            ['git', 'log', '--format=%H', '--', file_path],
            cwd=repo_root,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if not commits.stdout:
            # fallback: use the last commit date for the file
            last = subprocess.run(
                ['git', 'log', '-1', '--format=%aI', '--', file_path],
                cwd=repo_root,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            if last.stdout and last.stdout.strip():
                date_obj = datetime.fromisoformat(last.stdout.strip().replace('Z', '+00:00'))
                return date_obj.strftime('%Y-%m-%d %H:%M:%S %z')
            return None

        hashes = [h.strip() for h in commits.stdout.splitlines() if h.strip()]

        for h in hashes:
            # Inspect the patch for this commit for the given file
            show = subprocess.run(
                ['git', 'show', h, '--', file_path],
                cwd=repo_root,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            patch = show.stdout or ''

            # Find added/removed lines in the patch (skip file headers like '+++').
            significant = False
            for line in patch.splitlines():
                if line.startswith('+++') or line.startswith('---'):
                    continue
                if line.startswith('+') or line.startswith('-'):
                    # Ignore lines that only touch the updated_at field
                    if re.match(r'^[+-]\s*updated_at:', line):
                        continue
                    # Ignore empty additions/removals
                    if line.strip() in ('+', '-'):
                        continue
                    significant = True
                    break

            # If this commit contains a significant change, return its date
            if significant:
                date_res = subprocess.run(
                    ['git', 'show', '-s', '--format=%aI', h],
                    cwd=repo_root,
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )
                if date_res.stdout and date_res.stdout.strip():
                    date_obj = datetime.fromisoformat(date_res.stdout.strip().replace('Z', '+00:00'))
                    return date_obj.strftime('%Y-%m-%d %H:%M:%S %z')

        # If we didn't find any significant commit (e.g. only updated_at changes),
        # fallback to the most recent commit date for the file.
        last = subprocess.run(
            ['git', 'log', '-1', '--format=%aI', '--', file_path],
            cwd=repo_root,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if last.stdout and last.stdout.strip():
            date_obj = datetime.fromisoformat(last.stdout.strip().replace('Z', '+00:00'))
            return date_obj.strftime('%Y-%m-%d %H:%M:%S %z')
    except Exception as e:
        print(f"Error getting git date for {file_path}: {e}")
    return None

def update_post_frontmatter(file_path):
    """Update updated_at field in post frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        print(f"No frontmatter found in {file_path}")
        return False
    
    frontmatter = frontmatter_match.group(1)
    body = content[frontmatter_match.end():]
    
    # Get git date (last meaningful change)
    git_date = get_git_last_modified(file_path)
    if not git_date:
        print(f"Could not get git date for {file_path}")
        return False

    # If the frontmatter already has the same value, skip writing
    existing_match = re.search(r'updated_at:\s*(.+)', frontmatter)
    if existing_match:
        existing_val = existing_match.group(1).strip().strip('"\'')
        if existing_val == git_date:
            print(f"- {file_path}: up-to-date ({git_date})")
            return False
    
    # Update or add updated_at field
    if 'updated_at:' in frontmatter:
        frontmatter = re.sub(
            r'updated_at:.*$',
            f'updated_at: {git_date}',
            frontmatter,
            flags=re.MULTILINE
        )
    else:
        frontmatter += f'\nupdated_at: {git_date}'
    
    # Write back
    new_content = f'---\n{frontmatter}\n---\n{body}'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ {file_path}: {git_date}")
    return True

def main():
    """Update all posts in _posts directory."""
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '_posts')
    
    count = 0
    for root, dirs, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if update_post_frontmatter(file_path):
                    count += 1
    
    print(f"\n{count} posts updated.")

if __name__ == '__main__':
    main()
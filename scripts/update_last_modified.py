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
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%aI', file_path],
            cwd=os.path.dirname(__file__),
            capture_output=True,
            text=True
        )
        if result.stdout.strip():
            # Parse ISO format date and return in Jekyll format
            date_obj = datetime.fromisoformat(result.stdout.strip().replace('Z', '+00:00'))
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
    
    # Get git date
    git_date = get_git_last_modified(file_path)
    if not git_date:
        print(f"Could not get git date for {file_path}")
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
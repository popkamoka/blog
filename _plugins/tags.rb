module Jekyll
  class TagPageGenerator < Generator
    safe true

    def generate(site)
      puts "Génération des pages de tags..."  # Debug message
      tags = site.posts.docs.flat_map { |post| post.data['tags'] || [] }.to_set
      puts "Tags trouvés : #{tags.to_a}"  # Affiche les tags trouvés
      tags.each do |tag|
        site.pages << TagPage.new(site, site.source, tag)
      end
    end
  end

  class TagPage < Page
    def initialize(site, base, tag)
      puts "Initialisation de la page pour le tag : #{tag}"  # Message pour chaque page tag
      @site = site
      @base = base
      @dir  = File.join('tag', tag)
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag.html')
      self.data['tag'] = tag
      self.data['title'] = "Tag: #{tag}"
    end
  end
end

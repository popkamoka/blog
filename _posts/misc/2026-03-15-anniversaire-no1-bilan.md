---
layout: post
category: misc
title: "Anniversaire n°1 — bilan"
author: POPKAMOKA
date: 2026-03-15
tags: []

progress_status: completed
updated_at: 2026-03-15 15:04:59 +0100
---
Avec un petit jour d’avance, il est temps de célébrer le premier anniversaire de ce blog et d’en faire le bilan.

Je suis très content de cette première année, que ça soit en termes d’œuvres que j’ai pu découvrir ou du travail de rédaction des billets. Ce blog remplit d’ailleurs bien son objectif : je suis capable de voir en un clin d’œil ce que j’ai pu lire, regarder ou jouer cette année, le tout accompagné de notes personnelles plus ou moins développées. Je me suis même permis de rajouter un petit backlog d’œuvres que je dois me procurer ou explorer prochainement.

Bien que moins structuré qu'un système avec une vraie base de données, je suis globalement quand même satisfait de Jekyll et de la manière dont je structure mes articles. Comme je ne reviens généralement pas sur mes anciens billets, cette gestion plus artisanale fonctionne encore assez bien.

Parlons maintenant de ce qui fâche : ce blog a été construit sur base d'un template trouvé sur Internet, que j'ai modifié au fur et à mesure du temps en fonction de mes besoins, et ce, principalement via Copilot. Je ne peux pas nier qu'il a plutôt fait du bon boulot : j'ai eu ce que je voulais, organisé comme je le souhaitais, et ce, vraiment rapidement, de quoi me concentrer sur le contenu des articles plutôt que sur la forme. Il a été particulièrement utile pour tout ce qui est script Python de génération de billets.

J'ai cependant un rapport compliqué avec l'IA, en particulier à un stade de ma carrière où j'ai besoin d'apprendre et non pas devenir dépendant d'un outil qui risquera sans aucun doute de me desservir dans le futur.

J'aimerais donc repartir du template de base et recoder toutes les fonctions dont j'ai besoin moi-même : autant, je suis OK avec le fait d'utiliser l'autocomplétion ou poser des questions de temps en temps, autant, je ne veux pas tomber dans la facilité d'y avoir recours pour n'importe quel changement. Ce blog est un projet personnel et développé pour mon plaisir, je peux donc totalement me permettre d'en faire une expérience d'apprentissage de développement.

Je me pose aussi quelques questions par rapport aux technologies utilisées pour ce blog, surtout étant donné qu'il grandit plutôt vite. J'avais voulu éviter d'utiliser un SGBD par facilité d'utilisation et d'hébergement, mais je commence à me poser la questiodn de si ça ne vaudrait pas la peine de le migrer. Je pense notamment aux points suivants qui suscitent ce questionnement :

> La génération d'articles se fait pour l'instant via un script Python, je n'ai pas d'interface dédiée pour en créer ou en éditer facilement sans passer par Git.
>
> Les tags ne fonctionnent pas à cause d'un plugin non-compatible avec GitHub Pages.
>
> Les dates de mise à jour de l'article sont également maintenues via un script Python que je lance à la main.
>
> Je n'ai rien en place pour la gestion d'assets et d'images, notamment en termes de redimensionnement.
>
> Le tri d'articles et la pagination sont quasi inexistants.
>
> En mode développement, le blog prend bien plus de 5 secondes pour recharger une page après un changement.

Je pense donc me renseigner un peu sur ce qui existe comme alternative à Jekyll, mais je compte de toute façon nettoyer un peu ce repo pour me le réapproprier. Dans tous les cas, le fond des articles ne changera pas, ce qui reste le cœur de ce blog.

Nous verrons donc où nous en serons en 2027, mais d'ici là, j'espère avoir l'occasion de découvrir de nouvelles œuvres dont les billets viendront alimenter ce blog. À l'année prochaine !

**— Popka**

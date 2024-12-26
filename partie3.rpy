label start3:
    scene cirque_exterieur with fade
    show Barbara at breathe_right with dissolve
    show Christopher at breathe_left with dissolve
    stop sound fadeout 1.0
    play music "circus3.mp3" fadein 1.0
    "Le lendemain matin, le soleil se lève doucement sur le cirque, mais l'atmosphère est loin d'être apaisée. Christopher et Barbara étaient arrivés tôt pour reprendre l'enquête."
    
    if knowsAboutChild == False:
        B "Christopher, j'ai parlé à Rosalie hier soir. Elle m'a révélé quelque chose d'étonnant… Lucien avait un autre enfant, bien avant Oliver."
        
        C "Un autre enfant ? Pourquoi n'en a-t-il jamais parlé ? Et qu'est-il devenu ?"
        
        B "Rosalie n'en sait pas beaucoup. Lucien n'a jamais voulu en parler. Mais cet enfant pourrait être la clé de toute cette affaire."
        
        $ knowsAboutChild = True
    
    C "Nous avons plusieurs pistes, mais quelque chose continue de nous échapper. Tout semble tourner autour de Lucien, mais pourquoi garderait-il un secret aussi lourd ?"
    
    B "Il y a cette rumeur... Cet enfant dont Rosalie a vaguement parlé. Mais il n'a jamais été mentionné dans les registres officiels. Pas de photos, pas de traces de cet enfant. C'est comme s'il n'avait jamais existé."
    
    C "Et pourtant, si cet enfant était une pièce centrale du puzzle, pourquoi personne n'en parlerait ouvertement ?"
    
    "Christopher réfléchit un instant, fronçant les sourcils."
    
    C "Si c'est à ce moment qu'il a changé, il devait y avoir quelque chose qui le hantait. Quelque chose de si important qu'il a tout fait pour le cacher."
    
    "Barbara hoche la tête, pensant aux derniers indices."
    
    B "Il y a sûrement un endroit lié à cette époque, un lieu symbolique pour lui. C'est peut-être là qu'on trouvera des réponses. Mais où chercher ?"
    
    menu:
        "Fouiller le bureau de Lucien":
            jump fouiller_bureau_lucien
        "Réexaminer la lettre trouvée dans la roulotte de Lucien":
            jump réexaminerlalettre


label réexaminerlalettre:
    C "Nous avions trouvé une lettre, n'est-ce pas ? Pouvez-vous relire le contenu ?"
    
    B "'Je ne peux plus continuer ainsi, cette place devait être mienne… je te retrouverai et la reprendrai, que tu le veuilles ou non.' La signature est illisible."
    
    C "Cette lettre pourrait indiquer que Lucien était sous pression ou avait un conflit majeur avec quelqu'un. Peut-être que cette personne a un lien avec l'enfant ou le secret qu'il cachait."
    
    "Barbara semble réfléchir."
    
    B "Le ton de cette lettre est désespéré et accusateur. Lucien devait craindre quelque chose ou quelqu'un, probablement lié à l'enfant ou à ses propres actions."
    
    jump fouiller_bureau_lucien


label fouiller_bureau_lucien:
    scene bureauL
    show Barbara at breathe_right
    show Christopher at breathe_left
    "Vous entrez dans le bureau de Lucien. L'atmosphère est étrange, marquée par l'absence du propriétaire. "
    "Christopher et Barbara fouillent minutieusement chaque recoin, espérant trouver un indice caché."
    
    B "Il y a peut-être quelque chose ici qui nous échappe. Lucien était un homme méthodique, il devait laisser des indices."
    
    "Après avoir exploré divers tiroirs et étagères, Barbara découvre un compartiment secret sous un panneau de bois." 
    "Elle l'ouvre pour révéler une boîte en métal ancienne, rouillée."
    
    B "Voyons ce qu'il y a à l'intérieur."
    
    "Elle ouvre la boîte avec précaution, révélant plusieurs documents. Parmi eux, un dossier jauni, portant des dates et des notes écrites à la main. Barbara lit à voix haute."
    
    B "'Je ne peux plus supporter ce secret. L'enfant devait être éloigné… Je le garderai hors de ce cirque, mais je devrai faire des choix difficiles.'"
    
    "Christopher fronce les sourcils."
    
    C "Cela confirme que Lucien a pris des mesures drastiques pour cacher cet enfant. Mais où pourrait-il avoir emmené l'enfant, et pourquoi est-ce si important ?"
    
    "Barbara continue de chercher dans la boîte et trouve une vieille photo d'un endroit que Lucien semblait visiter souvent."
    
    B "Il semble que Lucien avait un lieu préféré, un endroit où il se rendait souvent pour réfléchir. Cet endroit est lié à l'enfant et à ses secrets."
    
    C "Allons-y."
    
    jump fouiller_chapiteau_abandonné

label fouiller_chapiteau_abandonné:
    scene chapiteau with fade
    show Barbara at breathe_right
    show Christopher at breathe_left
    C "Nous y voilà, l'ancien chapiteau…"
    B "Il a été abandonné depuis des années, mais il reste encore des traces de ce qu'il a été autrefois."
    
    "L'atmosphère est lourde, remplie de poussière et d'humidité. Les pas de Christopher et Barbara soulèvent de légers nuages gris, tandis qu'une brise légère fait flotter les vieilles tentures déchirées. Le chapiteau est devenu un cimetière silencieux de souvenirs."

    C "Regarde ça, Barbara. Un véritable chaos... Mais ces papiers pourraient nous en dire plus sur ce que Lucien cachait."
    B "Cet endroit renferme plus de secrets qu'il n'y paraît. Si nous prenons le temps, peut-être trouverons-nous ce que Lucien essayait de dissimuler."

    menu:
        "Fouiller les papiers cachés dans le bureau":
            jump fouiller_papiers

        "Fouiller près de l'arbre":
            jump fouiller_arbre

label fouiller_arbre:
    "Près d'un grand arbre mort qui domine la scène, une petite croix de bois à moitié enfouie marque une tombe anonyme."

    B "Cette tombe… Il n'y a aucun nom. Qui a été enterré ici, et pourquoi personne n'en parle jamais ?"
    C "Il est temps de découvrir ce qu'elle cache."

    menu:
        "Ouvrir la tombe":
            jump ouvrir_tombe

        "Retour au bureau":
            jump fouiller_papiers

label ouvrir_tombe:

    "En ouvrant la tombe délicatement, Christopher et Barbara découvrent un vieux morceau de papier soigneusement plié."

    B "'Ma fille n'a jamais eu sa chance. Je l'ai emportée loin du cirque... Elle est morte. Je devais le faire.'"
    
    C "Lucien a emporté sa propre fille, et elle est morte. Ce secret pesait sur lui depuis toutes ces années."
    
    B "Tout prend un sens maintenant. Cet enfant est la clé de tout."
    
    menu:
        "Retour au bureau":
            jump fouiller_papiers

label fouiller_papiers:
    C "Voyons ce que ces papiers nous disent..."
    "Christopher trie soigneusement les papiers retrouvés dans le bureau en ruine. Il déplie une série de notes manuscrites."

    C  "'Émile semble trop proche de Rosalie. Je dois m'assurer qu'il reste éloigné d'elle. Si je n'ai pas droit au bonheur, pourquoi elle y aurait-elle droit ?'"
    
    B "Lucien voulait séparer Émile et Rosalie... Mais pourquoi ?"
    
    C "'Zuddy devient de plus en plus pressant. S'il continue à me menacer de quitter le cirque, tout pourrait s'effondrer.'"
    
    B "Zuddy aussi le mettait sous pression. Il est clair que Lucien était entouré de conflits personnels."

    C "'Oliver refuse de prendre la direction du cirque. Il ne veut pas hériter des responsabilités. Je dois trouver un moyen de le persuader. Je n'ai pas fait tout cela pour rien"
    B "Il était donc coincé, tiraillé entre son fils qui refusait de reprendre le flambeau et Zuddy qui devenait une menace directe."
    menu:
        "Fouiller près de l'arbre":
            jump fouiller_arbre

        "Terminer la fouille":
            jump terminer_fouille

label terminer_fouille:
    "En terminant leur fouille, Barbara trouve un vieux coffre caché sous des débris. En l'ouvrant, elle découvre un recueil de poèmes, usé par le temps."

    B "'Carme, je t'aime et t'aimerai toujours.'"
    C "Un recueil de poèmes d'amour... Lucien aimait encore Carme, malgré tout ce qui se passait."
    B "Cette passion cachée a pu mener à sa chute."
    B "Le soleil va bientôt se coucher... Il est temps de confronter celui qui a tué Lucien."

    menu:
        "Accuser Émile d'avoir tué Lucien.":
            jump accuser_emile

        "Accuser Rosalie d'avoir tué Lucien.":
            jump accuser_rosalie

        "Accuser Oliver d'avoir tué Lucien.":
            jump accuser_oliver

        "Accuser Zuddy d'avoir tué Lucien.":
            jump accuser_zuddy

        "Accuser Carme d'avoir tué Lucien.":
            jump accuser_carme

label start:
    play music "début.mp3" fadein 1.0
    scene bureau
    with fade
    show Christopher at breathe_left

    "Christopher Lambert était assis dans son bureau, le regard perdu sur les dossiers empilés devant lui. Cela faisait des semaines qu'il n'avait pas été assigné à une nouvelle enquête."
    "Le silence pesant de la pièce n'était rompu que par le bruit lointain des voitures qui passaient dans la rue."
    
    "Depuis ce jour où il avait bu lors d'une mission, tout avait changé. Il avait mis en danger ses collègues... et pire encore, Barbara."
    "Son assistante. La personne qui croyait le plus en lui avant cet incident. Leur relation, autrefois professionnelle et respectueuse, s'était effritée, laissant place à une tension palpable à chaque échange."

    "Il soupira profondément, se demandant combien de temps encore il serait laissé à l'écart, emprisonné dans ses propres regrets. La culpabilité le rongeait, mais l'inaction était pire."
    "Il avait besoin de reprendre du service, de se prouver qu'il était toujours le détective qu'il avait été."

    "Alors qu'il se noyait dans ses pensées, un coup retentit à la porte, le tirant brusquement de sa torpeur."

    menu:
        "Ne pas répondre":
            jump silence1

        "Dire à la personne d'entrer":
            jump repondre1

label silence1:

    "Un silence pesant s'installa alors que Christopher restait immobile, les yeux rivés sur le bureau. L'espace d'un instant, il espérait peut-être que l'intrus s'en irait."
    "Mais après quelques secondes, la porte s'entrouvrit lentement."

    "Son assistante, mademoiselle Barbara Vincent, apparut dans l'entrebâillement, visiblement mal à l'aise."
    show Barbara at breathe_right
    with fade
    "Cela faisait des semaines qu'elle l'ignorait et l'évitait, affichant une froideur implacable à chaque rencontre. Leur relation, autrefois professionnelle et fluide, n'était plus que l'ombre d'elle-même."

    "Malgré son jeune âge, Barbara avait su se rendre indispensable à l'agence."
    "Son oncle, un homme influent et fortuné, injectait régulièrement des fonds à la petite agence de détectives qu'ils formaient, ce qui avait permis à Barbara de travailler avec eux."
    "Mais ses compétences ne laissaient personne douter de sa légitimité ici. Elle était brillante, futée, et personne n'avait osé la traiter avec condescendance."

    "Barbara toussa légèrement, cherchant à briser la tension et à attirer l'attention de Christopher."

    B "Le chef nous a transmis une enquête."

    menu:
        "Rester dans le silence":
            jump silence2

        "Demander plus de détails":
            jump repondre2

label repondre1:

    C "Oui ?"

    "La porte s'ouvrit, révélant son assistante, mademoiselle Barbara Vincent. Elle se tenait droit devant lui, visiblement partagée entre le malaise et un certain professionnalisme froid."
    show Barbara at breathe_right
    "Depuis cet incident, elle n'avait pas cherché à lui adresser un mot de plus que nécessaire."
    "Christopher remarqua une lueur d'hésitation dans son regard, comme si elle cherchait quelque chose, une réassurance peut-être. Mais il savait qu'il ne pourrait pas la lui donner."

    "Barbara, malgré la tension palpable entre eux, était restée à l'agence."
    "Son jeune âge ne lui avait pas posé d'obstacles ici, surtout grâce aux dons réguliers de son oncle, un mécène discret mais influent. Mais plus que ses relations, c'étaient ses compétences indéniables qui lui avaient assuré une place au sein de l'équipe."
    "Brillante et débrouillarde, elle avait prouvé qu'elle valait bien plus que son nom."

    B "Le chef nous a transmis une enquête."

    menu:
        "Rester dans le silence":
            jump silence2

        "Demander plus de détails":
            jump repondre2
label silence2:

    B "Bon, écoutez, moi aussi je suis gênée de la situation, et pourtant, je fais un effort devant vous." 
    B "Serait-ce trop difficile de réagir ? Ou bien ne suis-je plus digne de votre attention ?"

    "Barbara fixait Christopher avec une froideur qui trahissait une certaine tristesse derrière la colère."
    "Elle avait été patiente, mais visiblement, son silence commençait à la lasser."

    C "Barbara, je..."

    B "Non, je ne veux rien entendre finalement." # Elle le coupe, visiblement frustrée.

    B "Nous devons nous dépêcher." 
    B "Il y a quelques jours, un directeur de cirque a été assassiné dans sa roulotte, et les policiers en charge de l'enquête ont conclu que cela ne pouvait être qu'un vol qui a mal tourné, un crime de passage."

    "Elle fit une pause, laissant ses mots peser dans l'air."

    B "Son fils, cependant, ne croit pas à cette version des faits et a fait appel à nos services." 
    B "Il est persuadé qu'un membre du personnel du cirque est le coupable."

    "Barbara croisa les bras, attendant une réponse de Christopher, mais il restait toujours silencieux, troublé par leur échange." 
    "Il se demandait comment cette enquête pourrait changer leur dynamique ou s'il allait encore empirer la situation."

    menu:
        "Descendre au cirque":
            jump cirque

label repondre2:

    C "Et bien, donne-moi plus de détails."

    B "Il y a quelques jours, un directeur de cirque a été assassiné dans sa roulotte." 
    B"Les policiers en charge de l'enquête ont conclu que c'était probablement l'œuvre d'un voleur de passage."

    B "Cependant, son fils n'est pas convaincu."
    B "Il a fait appel à nous car il est persuadé que le coupable se trouve parmi les membres du personnel du cirque."

    C "Quand attend-il notre visite ?"

    B "Le chef a dit que nous serions sur place dans une heure."

    C "Bien, descendez, je vous rejoins dans un instant."

    "Barbara acquiesça, sans un mot de plus, puis tourna les talons pour partir." 
    "Christopher l'observa sortir, la tension toujours présente dans l'air. Peut-être que cette enquête offrirait une chance de réparer leur relation."

    menu:
        "Descendre au cirque":
            jump cirque


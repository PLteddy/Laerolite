label cirque:
    $ saitCarme = False
    $ saitZuddy = False  
    $ saitRosalie = False
    $ saitFemme = False
    $ saitLettre = False
    $ saitEmile = False  # Variable pour Émile
    scene black
    "Le trajet s'était fait dans un silence lourd de non-dits."
    "Christopher, perdu dans ses pensées, tentait de repousser ses tourments personnels pour se concentrer sur l'enquête à venir."
    "Barbara, assise à ses côtés, ne prononça pas un mot, fixant le paysage défilant par la fenêtre."

    "Arrivés enfin au cirque, une étrange atmosphère régnait sur le lieu. Les tentes colorées semblaient fanées sous le poids de la tragédie, et l'air était saturé d'un silence pesant."
    "Ils furent rapidement accueillis par Oliver Remaut, le fils de la victime."
    scene cirque_exterieur
    stop sound fadeout 1.0
    play music "circus2.mp3" fadein 1.0
    show Barbara at breathe_right
    show oliver at breathe_center
    show Christopher at breathe_left
    with fade

    "Oliver, un homme d'une vingtaine d'années, avait les traits tirés, le visage marqué par des cernes profondes." 
    "Ses yeux, nerveux et en perpétuel mouvement, scrutaient les environs comme s'il redoutait une menace invisible, prête à surgir."

    O "Ah enfin, vous voilà. J'ai beaucoup hésité avant de faire appel à vos services, mais désormais je suis certain que vous êtes la clé pour résoudre cette affaire."

    "Christopher, fidèle à lui-même, ne laissa rien transparaître. Son regard froid et analytique détailla rapidement Oliver, cherchant déjà des indices dans son comportement."
    "Il ne perdit pas de temps en politesses."

    C "Allons droit au but, si vous voulez bien. Le temps presse."

    "Oliver, visiblement un peu déstabilisé par la froideur de Christopher, acquiesça néanmoins sans objection."

    O "Oui, bien sûr. Que voulez-vous savoir ?"

    menu:
        "Demander des détails sur la victime":
            jump detailsvictime

        "Demander des détails sur l'organisation du cirque":
            jump detailscirque

        "Demander à voir la scène du crime":
            jump sceneducrime

label detailscirque:

    C "Racontez-moi comment ce cirque est organisé, qui sont les principaux membres, et comment les choses fonctionnaient avec votre père à la tête."

    "Oliver sembla réfléchir, son regard se perdant dans le passé."

    O "Le cirque l'Aérolite a toujours fonctionné comme une grande famille... Enfin, c'est ce que mon père aimait dire devant les clients. En réalité, il y avait beaucoup de tensions."

    O "Les membres du personnel les plus influents sont Zuddy, le clown principal, Madame Carme Peri, la voyante, et Émile, le mime acrobate." 
    O "Ces trois-là étaient les plus proches de mon père, mais aussi ceux qui auraient pu monter quelque chose contre lui sans que personne n'ose parler."

    O "Je suis certain que l'un d'entre eux est le coupable. Mon père se méfiait d'eux, même s'il n'en parlait jamais directement."

    "Christopher observa attentivement Oliver, notant l'amertume dans sa voix. Il sentait que ce fils connaissait bien plus de secrets qu'il n'était prêt à révéler d'un coup."

    menu:
        "Demander des détails sur Zuddy":
            jump detailZuddy

        "Demander des détails sur Carme Peri":
            jump detailCarme

        "Demander des détails sur Émile":
            jump detailEmile

        "Poser une autre question à Oliver":
            jump autre_question

label detailCarme:

    C "Et que pouvez-vous me dire sur Madame Carme Peri, la voyante ?"

    "Oliver prit un moment avant de répondre, comme si évoquer Carme le troublait."

    O "Carme... Elle est une figure intrigante, presque énigmatique. C'est la première à avoir rejoint le cirque, bien avant même que mes parents ne se marient."

    O "Elle a toujours été très proche de mon père, surtout durant mon enfance. Peut-être trop proche au goût de ma mère."

    "Il baissa la voix, comme s'il craignait que quelqu'un puisse l'entendre."

    O "Carme et mon père avaient un lien particulier. Il la consultait souvent pour des 'conseils'. Mon père avait cette fascination pour l'ésotérisme, et elle savait parfaitement en jouer."
    O "Mais il y a quelque chose de plus sombre chez elle, quand elle me regarde je sens toujours une colère qui semble toujours prête à éclater."

    O "Il y a dix ans, quelque chose s'est passé. Carme est restée enfermée dans sa roulotte pendant des semaines, et depuis, elle n'est plus la même."
    O "Plus froide, plus distante. Mon père et elle se disputaient souvent après cela."

    O "Je ne sais pas ce qu'elle lui reprochait, mais ça les a profondément changés." 
    O "Elle est devenue une menace silencieuse, prête à frapper au moment où on s'y attendrait le moins."

    "Christopher enregistra mentalement ces informations, conscient que ce mystère autour de Carme pourrait bien être un indice important."
    $ saitcarme = True

    menu:
        "Demander des détails sur Zuddy":
            jump detailZuddy

        "Demander des détails sur Émile":
            jump detailEmile

        "Poser une autre question à Oliver":
            jump autre_question

label detailEmile:

    C "Et Émile, le mime acrobate ? Quelle était sa relation avec votre père ?"

    "Oliver fronça les sourcils, une ombre de mécontentement passant sur son visage."

    O "Émile est un homme compliqué. Il ne parle presque jamais, pas même en dehors de la scène." 
    O "Mon père disait toujours qu'il était un génie du spectacle, mais il a aussi quelque chose de dérangeant en lui."

    O "Il a été repéré dans un petit cirque en Roumanie, et mon père l'a tout de suite engagé." 
    O "Il voyait en lui un grand artiste, mais je pense qu'il n'a jamais totalement fait confiance à Émile."

    O "Émile est un observateur silencieux. Il sait tout ce qui se passe ici. Rien ne lui échappe." 
    O"Même les choses que personne ne remarque, lui les voit. Mais il reste distant, mystérieux. Il aurait pu orchestrer quelque chose, et personne ne s'en serait aperçu."

    O "Je ne sais pas s'il est coupable, mais je sais qu'il sait beaucoup plus que ce qu'il laisse paraître."

    "Christopher hocha la tête légèrement, réfléchissant à ce portrait d'un homme aussi secret qu'inquiétant."

    $ saitemile = True 

    menu:
        "Demander des détails sur Zuddy":
            $ saitZuddy = True
            jump detailZuddy

        "Demander des détails sur Carme Peri":
            jump detailCarme

        "Poser une autre question à Oliver":
            jump autre_question

label detailZuddy:

    C "Parlez-moi de Zuddy, le clown. Quel était son lien avec votre père ?"

    "Oliver sourit amèrement, comme si évoquer Zuddy réveillait des souvenirs douloureux."

    O "Zuddy, c'est... le pilier du cirque. Il est là depuis presque aussi longtemps que moi." 
    O"Mon père l'a toujours considéré comme un frère. Mais ne vous y trompez pas, sous son masque de clown se cache un homme calculateur et ambitieux."

    O "Zuddy savait comment manipuler les autres, et il voulait depuis longtemps avoir plus de contrôle sur le cirque." 
    O"Il pensait pouvoir prendre la place de mon père, mais celui-ci ne lui a jamais donné cette opportunité. Mon père le tenait à distance, car il savait qu'il était dangereux."

    O "Je ne serais pas surpris que Zuddy ait vu la mort de mon père comme une opportunité. Peut-être n'a-t-il pas agi seul, mais il est certainement l'un des principaux suspects."
    O "Il est capable de tout pour arriver à ses fins."

    "Christopher sentit le poids des accusations. Zuddy, le manipulateur caché sous un masque jovial, semblait être un suspect de premier plan."
    
    menu:
        "Demander des détails sur Carme Peri":
            jump detailCarme

        "Demander des détails sur Émile":
            jump detailEmile

        "Poser une autre question à Oliver":
            jump autre_question

label detailsvictime:
    C "Commençons par la victime. Parlez-moi de votre père."

    O "Mon défunt père, Lucien Remaut, dirigeait l'aérolite depuis plus de vingt ans." 
    O "Il était... difficile, très strict avec ses employés, mais je ne l'aurais jamais imaginé se faire assassiner. Certes, il n'était pas très aimé, mais qui aurait pu aller jusqu'à le tuer ?" 
    O "C'est ce que je ne comprends pas. Il ne méritait pas une telle fin. Il a toujours été un honnête homme."

    B "Hmm." 
    "Barbara hocha la tête, prenant note de chaque mot. Oliver quand son regard se posait sur elle était dédaigneux."

    menu:
        "Demander des détails sur la relation avec sa mère":
            jump questionfemme

        "Demander des détails sur l'organisation du cirque":
            jump detailscirque

        "Demander à voir la scène du crime":
            jump sceneducrime

label questionfemme:
    C "Parlez-moi de la relation entre votre père et votre mère. Est-ce qu'ils s'entendaient bien ?"

    O "Mes parents… Leur relation était loin d'être idéale. Ils étaient mariés depuis longtemps, mais avec les années, leur relation est devenue plus fade." 
    O"Mon père, Lucien, ne pensait qu'au cirque. Ce spectacle, c'était toute sa vie, et ma mère en souffrait beaucoup. Elle n'a jamais voulu cette vie nomade, mais elle l'a supportée pour lui… au début du moins."

    O "Ces dernières années, ils vivaient presque comme des étrangers." 
    O"Ma mère rêvait de stabilité, d'une vie plus tranquille. Ils se disputaient souvent... Je sais qu'elle a même envisagé de le quitter à plusieurs reprises, mais elle est restée, pour moi je suppose."
    O "Pourtant, il n'y avait plus d'amour entre eux, juste une habitude. Ils s'apportaient du réconfort, mais c'était tout."

    C "Hmm..." 
    "Christopher nota mentalement que ce mariage semblait être une source de tension. Peut-être y avait-il plus à découvrir sur sa femme."

    menu:
        "Demander si elle pourrait être impliquée":
            jump implicationfemme

        "Poser une autre question à Oliver":
            jump autre_question

label implicationfemme:
    B "Pensez-vous qu'ils auraient pu être assez en mauvais termes pour que votre mère fasse quelque chose ? Même involontairement ?"

    O "C'est pour cela que je pense que les femmes ne devraient pas essayer d'imiter les hommes en travaillant."

    "Barbara rougit, se sentant honteuse après la remarque cinglante d'Oliver."

    C  "Monsieur, je vous prierai de vous excuser envers mon assistante. Vos propos sont irrespectueux. Toute question est bonne à poser."
    "Oliver roula des yeux avant de s'excuser avec réticence."
    O  "Mes excuses..." 
    $ saitfemme = True

    menu:
        "Poser une autre question à Oliver":
            jump autre_question

label sceneducrime:
    C "Avant toute chose, j'aimerais voir la scène du crime."

    O "Bien sûr, suivez-moi."

    "Oliver hésita un instant, puis hocha la tête. Il les conduisit à travers le campement du cirque, jusqu'à une vieille roulotte peinte de couleurs fanées mise à l'écart de toutes les autres. L'atmosphère devenait lourde à mesure qu'ils approchaient."

    scene lucien

    O "C'est ici que mon père a été retrouvé... Je vous laisse fouiller, mais sachez que la police a déjà tout inspecté."

    "Christopher observa l'intérieur de la roulotte. Malgré les fouilles, quelques détails semblaient passer inaperçus."

    menu:
        "Examiner l'intérieur de la roulotte":
            jump investiguerroulotte

        "Interroger Barbara sur ce qu'elle a trouvé":
            jump questionneroliver

        "Poser une autre question à Oliver":
            jump autre_question


label investiguerroulotte:
    "Christopher et Barbara entrèrent dans la roulotte. L'endroit était en piteux état : des meubles renversés, des papiers éparpillés un peu partout, et une odeur de renfermé flottait dans l'air." 
    "La scène parlait d'elle-même : ce n'était pas la police qui avait pu faire cela ainsi, soit la victime avait l'habitude du chaos, soit quelqu'un avait fouillé l'endroit après le meurtre. "

    "Barbara se pencha pour examiner un coin sous un meuble renversé."

    B "Regardez ça."

    "Elle tendit la main pour saisir un morceau de papier et le déplia soigneusement, révélant ce qui semblait être une lettre déchirée."

    B "C'est une partie d'une lettre... on dirait qu'elle a été écrite par quelqu'un proche de la victime."

    C "Qu'est-ce que ça dit ?"

    "Barbara lut à voix basse."

    B "'Je ne peux plus continuer ainsi, cette place devait être mienne… je te retrouverai et la reprendrai, que tu le veuilles ou non.'" 
    B "La signature est illisible, mais cette personne semblait furieuse."

    "Christopher fronça les sourcils en observant le morceau de papier, réfléchissant à ce que cela pouvait signifier. Une menace ? Une simple dispute ? En tout cas, cela offrait une nouvelle perspective sur les relations de la victime."

    B "Il y a aussi des traces de pas boueuses près de la porte… peut-être que quelqu'un est entré par effraction après le meurtre, ou c'est la victime qui a tenté de fuir quelqu'un."

    C "Des traces de pas d'homme."

    B "Du 45, effectivement cela nous orienterait plus vers un profil masculin."

    "Ils sortirent de la roulotte et allèrent rejoindre Oliver."

    $ saitlettre = True

    menu:
        "Poser une autre question à Oliver":
            jump autre_question


label questionneroliver:
    C "La police a-t-elle trouvé quelque chose d'intéressant lors de leur enquête ici ?"

    "Oliver hocha la tête, croisant les bras comme pour se protéger du froid imaginaire."

    O "Ils ont fouillé l'endroit de fond en comble, mais à vrai dire, ils n'ont rien trouvé de concluant." 
    O "Juste des choses ordinaire de toute enquête de ce type, comme des traces de boue et des meubles renversés." 
    O "Et bien évidemment, tous les objets de valeur ont été dérobés." 
    O"Selon eux, c'était probablement un voleur qui est entré par effraction, a tué mon père et s'est enfui avec tout ce qu'il y avait d'important."

    "Il marqua une pause, luttant avec ses souvenirs."

    O "Ils ont aussi trouvé cette lettre déchirée... Mais ils l'ont jugée sans importance, pensant que c'était juste une dispute mineure." 
    O"Je ne suis pas d'accord. Mon père avait des ennemis ici, dans le cirque même. C'est pour ça que je vous ai appelés. Je suis sûr que cette lettre et le meurtre sont liés."

    menu:
        "Poser une autre question à Oliver":
            jump autre_question


label autre_question:
    scene cirque_exterieur
    show Barbara at breathe_right
    show Oliver_talk at breathe_center
    show Christopher at breathe_left
    C "J'ai une autre question, s'il vous plaît."

    O "Oui ?"

    menu:
        "Demander des détails sur la victime":
            jump detailsvictime

        "Demander des détails sur l'organisation du cirque":
            jump detailscirque

        "Demander à voir la scène du crime":
            jump sceneducrime

        "Récapitulez ce que vous avez avec Barbara":
            jump misaupointbarbara
    hide Oliver_talk

label misaupointbarbara:
    scene cirque_exterieur
    show Barbara at breathe_right
    show Oliver at breathe_center
    show Christopher at breathe_left
    C "Merci pour vos réponses, monsieur. Si vous permettez, moi et mon assistante allons nous concerter pour décider comment nous allons procéder."

    O "J'ai du travail qui m'attend dans tous les cas. Merci à vous, monsieur."

    "Sans jeter un regard à Barbara, Oliver tourna les talons et repartit d'un pas rapide."

    hide Oliver with dissolve
    hide Oliver_talk with dissolve
    

    B "Quelle impolitesse !"

    C "Certes, mais ne lui en voulez pas trop. Il est sous pression..."

    B "Je n'attendais pas à ce que vous me défendiez dans tous les cas..."

    C "Non, Barbara, je..."

    B "Peu importe. Nous devrions récapituler ce que nous avons."

    C "Je vous laisse faire."

    "Barbara prend une profonde inspiration avant de commencer à lister les suspects :"

    if saitZuddy == True:
        ame "Je sais que tu aimes les chocolats, alors je t'en ai acheté !"
    if saitCarme == True:
        B "Carme, la voyante. La première chose à voir avec elle serait pourquoi elle s'était disputée avec Lucien. On ne s'éloigne pas soudainement d'une personne qu'on côtoie depuis des années sans une bonne raison."

    if saitEmile == True :
        B "Emile, le mime acrobate. Je ne sais pas trop quoi penser de lui. Il n'a pas l'air d'avoir de raison d'assassiner Lucien. Mais le fait qu'Oliver nous en a parlé signifie que cela cache peut-être quelque chose."

    if saitFemme == True :
        B "Il ne nous a pas beaucoup parlé de sa mère. Il faudrait voir si elle peut être impliquée dans l'affaire ou non. C'est étrange qu'elle ne nous ait pas accueillis avec Oliver."

    else:
        C "J'ai entendu dire qu'il y avait d'autres suspects que nous n'avons pas encore interrogés. Voici ce que j'ai :"
        C "Zuddy, le clown, Carme, la voyante, Émile, le mime acrobate, et la femme de Lucien."
        B "Oui, effectivement, nous devrions leur parler pour éclaircir cette affaire."

    B "Donc voilà où nous en sommes pour l'instant. Mais il manque encore des pièces au puzzle."

    C "En effet. Nous devons continuer à interroger ces personnes et trouver ce qui les lie réellement à Lucien."

    B "Je me demande si le coupable est vraiment parmi ces suspects."

    C "À nous de le découvrir."

    menu:
        "Partie 2 : Les suspects":
            jump partie2

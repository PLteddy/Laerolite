label partie2:
    stop sound fadeout 1.0
    play music "circus.mp3" fadein 1.0
    C "Bon, par qui commençons-nous ?"
    
    B "Laissons le clown pour la fin, étant donné sa position dans le cirque, il pourrait nous apprendre des éléments après avoir discuté avec les autres."

    menu:
        "Interroger Émile":
            jump emileinterro
        "Interroger Carme":
            jump Carmeinterro
        "Interroger la femme de Lucien":
            jump femmeinterro

label emileinterro:
    scene scene_emile
    " Malgré leur présence Emile resta concentré sur le paysage au loin,les bras croisés, son visage fermé, affichant une expression distante."
    show Emile_regard_ailleurs at breathe_center
    show Barbara at breathe_right
    show christopher at breathe_left
    "Barbara regardait Christopher, attendant qu'il engage la conversation comme à son habitude."
    hide Emile_regard_ailleurs
    show Emile at breathe_center
    $ Emile = True

    menu:
        "Parler de Madame Remaut":
            jump rosalieemile
        "Parler de Carme":
            jump carmeemile
        "Parler de Zuddy":
            jump Zuddyemile
        "Engager la conversation":
            jump EngagerConversationseul
        "Laisser Barbara commencer":
            jump LaisserBarbara

label rosalieemile:
    E "Madame Remaut est une femme respectable. Les autres ne la voient pas de la même manière, mais je crois qu'ils se trompent. Elle est simplement... mal à sa place ici."

    menu:
        "Parler de Carme":
            jump carmeemile
        "Parler de Zuddy":
            jump Zuddyemile
        "Engager la conversation":
            jump EngagerConversationseul
        "Laisser Barbara commencer":
            jump LaisserBarbara

label carmeemile:
    E "Carme est la personne la plus digne du cirque. Toujours calme, elle ne dit jamais un mot de trop. Si je devais faire confiance à quelqu'un ici, ce serait à elle."
    hide Emile 
    show emile_happy at breathe_center
    menu:
        "Parler de Madame Remaut":
            jump rosalieemile
        "Parler de Zuddy":
            jump Zuddyemile
        "Engager la conversation":
            jump EngagerConversationseul
        "Laisser Barbara commencer":
            jump LaisserBarbara

label Zuddyemile:
    E "Zuddy... il est plus malin qu'il en a l'air. Il joue toujours le rôle du clown, mais ne vous y trompez pas. Il voit tout, et rien ne lui échappe."
    hide emile_happy
    show Emile at breathe_center
    menu:
        "Parler de Madame Relaut":
            jump rosalieemile
        "Parler de Carme":
            jump carmeemile
        "Engager la conversation":
            jump EngagerConversationseul
        "Laisser Barbara commencer":
            jump LaisserBarbara

label EngagerConversationseul:
    C "Bonjour Émile. Nous sommes des détectives mandatés par Oliver Remaut. J'aimerais vous poser quelques questions à propos de Lucien Remaut."
    
    E "..."
    
    # Émile reste silencieux un moment, observant Christopher et Barbara avec un regard froid.
    
    E "Je ne suis pas sûr que mes réponses vous seront utiles, mais je vous prie, détective."
    
    menu:
        "Poser des questions seul.":
            jump questionsdirectes
        "Laisser Barbara poser des questions.":
            jump douceur

label questionsdirectes:
    C "Bien. Étiez-vous proche de Lucien ? Il me semble que vous avez été repéré alors que vous faisiez partie d'une autre troupe."
    C "Pourquoi avoir quitté vos anciens camarades pour venir à l'Aérolite ?"
    
    E "Nous travaillions ensemble, c'est tout. C'était mon patron et nous avions une relation comme n'importe quel autre employé avec son chef." 
    C "Il n'y avait rien de spécial entre nous, sauf peut-être avec Zuddy et Carme. Mais vous devez déjà le savoir, surtout si c'est Oliver qui vous a accueillis."
    
    C "Il nous a effectivement dit que vous étiez au courant de presque tout ce qui se passait au cirque. Vous n'avez rien vu le jour du meurtre ?"
    
    E "Oliver a ses propres préjugés sur les gens du cirque. Son père l'a toujours maintenu à distance de... nous. Je ne sais rien de plus que n'importe qui ici."
    
    C "Quand avez-vous parlé à Lucien pour la dernière fois ?"
    
    E "Je ne me souviens plus exactement. C'est généralement Zuddy qui fait le lien entre le patron et nous. Peut-être pour la paie du mois dernier."
    
    C "D'après vous, qui aurait pu avoir le plus de raisons d'en vouloir à Lucien ?"
    
    E "Écoutez, je vais rester courtois, mais sachez qu'aucun de nous ici, au cirque, ne dénoncera un autre aux policiers ou aux détectives. Vous feriez mieux de partir maintenant."
    
    # Émile commence à se refermer et montre clairement qu'il ne souhaite plus parler.
   
    menu:
        "Essayer de percer son silence.":
            jump percer_silence
        "Terminer l'interrogatoire.":
            jump termineremile

label percer_silence:
    C "Je comprends, mais si vous saviez quoi que ce soit, cela pourrait vraiment nous aider dans cette enquête."
    
    E "..."
    "Émile ne dit plus un mot, fixant Christopher avec indifférence. Il semble déterminé à ne plus coopérer."
    jump termineremile

label LaisserBarbara:
    "Christopher réfléchit à sa relation avec Barbara, conscient des disputes passées."
    "Barbara lui disait souvent qu'il était trop bourru. Cette fois, je vais la laisser mener la danse."
    
    "Barbara s'approche doucement d'Émile, prenant un ton respectueux."
    B "Émile... Je sais que tout cela est difficile, mais nous avons besoin de votre aide pour comprendre ce qu'il s'est passé avec Monsieur Remaut."
    
    "Émile semble surpris que ce soit Barbara qui prenne les devants."
    E "Je ne suis pas sûr que cela changera quoi que ce soit, mais je vais vous écouter."
    
    menu:
        "Laissez Barbara continuer":
            jump douceur
        "Reprendre les rênes de l'interrogatoire":
            jump interrompre


label interrompre:

    # Christopher parle
    "Christopher se remit en avant, Emile regarda Barbara qui avait perdu son petit sourire et qui s'était remise à écrire sur son carnet de note."

    C "Bien, étiez-vous proche de Lucien ? Il me semble que vous avez été repéré alors que vous étiez déjà dans une autre troupe. Pourquoi avoir abandonné vos anciens camarades pour venir à l'Aérolite ?"

    # Émile répond
    E "Nous travaillions ensemble, c'est tout. C'était mon patron et nous avions une relation comme celle de n'importe qui d'autre, mise à part sa famille et Zuddy ou Carme. Mais vous devez déjà être au courant, étant donné que c'est Oliver qui vous a accueillis."

    C "Il nous a également dit que vous étiez au courant de presque tout ce qui se passait. Vous n'avez rien vu le jour du meurtre ?"

    E "Oliver a des aprioris sur les gens du cirque. Son père a toujours fait attention à ne pas trop le mélanger à... nous. Je ne sais rien de plus que tout le monde."

    C "Selon vous, qui aurait pu en vouloir le plus à Lucien ?"

    E "Écoutez, je vais rester poli, mais sachez que jamais quelqu'un d'autre que la famille Remaut ne balancera des noms pour les policiers ou des détectives. Je vous prie de bien vouloir partir désormais."

    "Émile semble ne plus vouloir donner son attention aux détectives..."

    # Choix du joueur
    menu:
        "Essayer de percer son silence.":
            jump percer_silence
        "Terminer l'interrogatoire.":
            jump termineremile

label douceur:
    "Barbara continue avec douceur, rayonnant de fierté. Christopher garde un ton calme et respectueux."
    B "Oliver nous a dit que vous étiez au courant de presque tout ce qui se passait au cirque. Vous n'avez rien vu le jour du meurtre ?"
    
    E "Oliver a des préjugés sur les gens du cirque. Son père a toujours fait attention à ne pas trop le mélanger à... nous. Je ne sais rien de plus que tout le monde. Si c'était le cas, je l'aurais dit."
    
    C "Quand avez-vous parlé à Lucien pour la dernière fois ?"
    
    E "Je ne sais plus. C'est généralement Zuddy qui gère la communication entre Lucien et nous. Peut-être pour la paie du mois dernier."
    
    B "Est-ce que sa mort vous a affecté ?"
    
    E "Pour être honnête avec vous, personne n'est vraiment triste. Lucien avait changé, sa passion pour le spectacle s'était transformée en une passion pour l'argent. Seule Rosalie et Oliver sont affectés."
    hide emile_happy
    hide Emile
    show emile_blush at breathe_center
    
    "Un silence gênant s'installe, et Émile semble regretter ce qu'il vient de dire. Barbara et Christopher échangent un regard intrigué."
    menu:
        "Appuyer sur Rosalie":
            jump appuyer
        "Changer de sujet":
            jump changersujet

label appuyer:
    "Barbara enfonce le clou, cherchant à en savoir plus sur la relation entre Émile et Rosalie."
    B "Rosalie ? Vous parlez de Mme Remaut ?"
    
    "Émile devient rouge pivoine, visiblement embarrassé."
    hide emile_blush
    show emile_smile_blush_regard_ailleurs at breathe_center
    E "Pas plus que tout le monde..."
    
    C "Vous êtes pourtant le seul à prononcer son prénom avec autant d'aisance."
    
    # Barbara poursuit, son ton doux mais insistant.
    B "Vous êtes devenus proches, n'est-ce pas ?"
    
    E "Rosalie... elle était différente avant. Elle détestait ce cirque, voire le haïssait. Mais..."
    E "Mais j'ai été témoin d'une scène de faiblesse de sa part, et cela nous a rapprochés. Elle apprécie un peu plus le cirque désormais, enfin... j'aimerais le croire."
    hide emile_smile_blush_regard_ailleurs
    show emile_shy at breathe_center
    "Barbara observe Émile, qui semble perdu dans ses pensées."
    B "Je vois. Vous semblez... la comprendre mieux que quiconque."
    
    # Émile murmure presque inaudiblement.
    E "C'est ce que j'espère..."
    
    $ emileConfession = True
    hide emile_shy
    jump termineremile


label changersujet:
    "Christopher décide de ne pas insister sur le sujet de Rosalie et ramène la discussion à Lucien et le cirque."
    C "Revenons à Lucien et au cirque. Vous avez dit que ses priorités avaient changé. Pouvez-vous préciser ?"

    E "Lucien... il était plus concentré sur les affaires que sur le spectacle ces derniers temps. Avant, tout tournait autour de la performance, de l'art, mais il a commencé à parler plus d'argent, de contrats, de partenariats."
    
    B "Pensez-vous que cela a pu créer des tensions avec les autres membres du cirque ?"
    
    E "Certainement. Zuddy en parlait souvent... il disait que Lucien oubliait ce qui faisait l'âme du cirque. Même Carme et Oliver avaient leurs réserves. "
    E "Je ne suis pas sûr de tout, mais les discussions devenaient plus tendues ces derniers mois."
    
    C "Est-ce qu'ils ont eu des confrontations directes avec Lucien à ce sujet ?"
    
    E "Pas des confrontations ouvertes... du moins, pas à ma connaissance. Mais il y avait des tensions. Zuddy, lui, se plaint toujours, mais Carme, quand elle se met à éviter quelqu'un, c'est mauvais signe."
    E "Quand a Oliver il se plaignait mais Lucien pensait que c'était un caprice d'enfant."

    jump termineremile



label termineremile:
    show Emile at breathe_center
    "L'interrogatoire prend fin. Émile reste silencieux alors que Christopher et Barbara quittent sa loge."
    C "Merci pour votre temps, Émile. Nous allons vous laisser."
    hide Emile with dissolve
    
    if emileConfession is True:
        B "Il aime une femme... et elle est maintenant libre. Est-ce que cela pourrait être un motif de meurtre ?"
    else:
        B "Nous n'avons pas appris grand chose malheureusement."
    menu:
        "Interroger Madame Remaut":
            jump femmeinterro
        "Interroger Carme":
            jump Carmeinterro
        "Finir par interroger Zuddy le clown":
            jump interroZuddy

label femmeinterro:
    scene scene_rosalie
    show Barbara at breathe_right
    show Rosalie at breathe_center
    show Christopher at breathe_left
    "Vous entrez dans la tente de Madame Remaut, décorée avec élégance mais marquée par une atmosphère glaciale."
    R "Vous devez être les détectives engagés par Oliver. Vous voulez sans doute parler de Lucien, n'est-ce pas ?"
    
    B "C'est exact, Madame Remaut. Nous comprenons que cela doit être une période difficile pour vous."
    
    R "Difficile ? Peut-être. Mais Lucien et moi... Nous n'étions pas proches."
    R "Il s'est marié avec moi pour mon titre, et moi pour son argent. Ce n'était pas une union d'amour."
    R "J'ai simplement perdu le père de mon fils. Je m'en remettrai."
    
    $ Rosalie = True
    if emileConfession:
        menu:
            "Poser une question sur la relation avec Émile.":
                jump relationemile
    else :
        menu:
            "Poser des questions sur Lucien.":
                jump LucienSecrets
            "Parler de Zuddy.":
                jump zuddyrosalie
            "Parler d'Émile.":
                jump emilerosalie

label carme:
    # Rosalie parle de Carme, révélant son opinion sur elle.
    R "Carme est une femme d'un certain mystère, mais elle reste toujours courtoise avec moi."
    R "Nous ne sommes pas proches, mais je respecte son travail et son calme. Elle sait garder ses distances et ses secrets."

    if emileConfession:
        menu:
            "Poser une question sur la relation avec Émile.":
                jump relationemile
    else :
        menu:
            "Terminer l'interrogatoire":
                jump terminerinterrof

label emilerosalie:
    R "Émile est... différent des autres. Il a toujours été plus réservé, mais il ne m'a jamais manqué de respect, contrairement à certains ici."
    R "Il semble me comprendre d'une manière que je ne saurais expliquer."

    if emileConfession:
        menu:
            "Poser une question sur la relation avec Émile.":
                jump relationemile
    menu:
        "Poser des questions sur Lucien.":
            jump LucienSecrets
        "Parler de Carme.":
            jump carmerosalie
        "Parler de Zuddy.":
            jump zuddyrosalie
    hide Rosalie

label zuddyrosalie:
    hide Rosalie
    show Rosalie_angry at breathe_center
    R "Zuddy... Je ne comprends pas pourquoi Lucien l'admirait autant. Il est vulgaire et irrespectueux. Je ne peux pas supporter sa présence, et il me le rend bien."
    
    if emileConfession:
        menu:
            "Poser une question sur la relation avec Émile.":
                jump relationemile
    menu:
        "Poser des questions sur Lucien.":
            jump LucienSecrets
        "Parler de Carme.":
            jump carmerosalie
        "Parler d'Émile.":
            jump emilerosalie

label relationemile:
    hide Rosalie_angry
    show Rosalie at breathe_center
    # Christopher interroge Rosalie sur Émile.
    C "Nous avons parlé à Émile, il semble être quelqu'un de respectueux envers vous."
    
    R "Émile est... différent des autres. Tous les autres membres du cirque me voient comme une intruse, quelqu'un qui n'appartient pas à leur monde." 
    R "Même si je me balade avec eux depuis plus de 20 ans. Mais Émile, lui, il est spécial à mon égard."

    B "Pensez-vous qu'il ait quelque chose à cacher ?"
    
    # Rosalie réfléchit un instant avant de répondre.
    R "Peut-être. Mais je doute qu'il soit impliqué dans tout ça. Il est fidèle, à sa manière. Plus fidèle que Lucien ne l'a jamais été, en tout cas."
    
    menu:
        "Revenir au sujet de Lucien.":
            jump LucienSecrets
        "Changer de sujet.":
            jump changersujetfemme

label changersujetfemme:
    
    C "Vous n'avez rien vu le jour du meurtre ?"
    
    R "Je n'étais pas au cirque mais en ville. En général, lorsque l'on s'arrête dans une grande ville, je réside dans un hôtel et non dans une tente ou quoi que ce soit d'autre."
    
    C "Quand avez-vous parlé à Lucien pour la dernière fois ?"
    
    R "Avant de partir, je lui ai demandé s'il voulait quelque chose, mais il avait l'esprit ailleurs. J'étais même étonnée, car il avait l'air triste, et cela ne lui arrivait jamais quand le cirque se portait aussi bien et faisait complet tous les soirs."
    
    C "Selon vous, qui aurait pu le plus en vouloir à Lucien ?"
    
    R "Je ne sais pas. Je ne suis pas au courant de tout ce qui se passe ici derrière les rideaux. Pour faire mon deuil, l'hypothèse du vol qui tourne en meurtre me suffit amplement."

    B "Et qui, à part vous et votre fils, était le plus proche de votre mari ?"
    
    R "Zuddy, le clown en chef, c'est le bras droit de mon mari et celui qui avait à peu près toute sa confiance. Sinon personne d'autre, même si à une autre époque j'aurais pu vous dire Carme."

    menu:
        "Poser des questions sur Carme.":
            jump carmerosalie
        "Terminer l'interrogatoire.":
            jump terminerinterrof
label carmerosalie:
    C "Vous vous entendez bien avec elle ? Il semblerait que votre mari et elle se soient éloignés parce que vous le lui aviez demandé."
    
    R "Je me fiche bien qu'il ait une maîtresse tant qu'il reste discret et qu'elle ne me manque pas de respect."
    
    B "Sans vouloir paraître grossière, je trouve cela étrange que vous ne soyez pas dérangée par cette idée."
    
    R "Je comprends, mais sachez qu'en réalité, Lucien devait épouser Carme." 
    R "Ils se connaissent depuis tout petits et ont eu l'idée du cirque ensemble. Mais, même si le cirque rapportait énormément, il lui manquait un titre pour que tous lui accordent du respect."

    R "Il a donc annulé son mariage avec elle et m'a épousée. Et pourtant, je n'ai jamais connu une femme aussi douce et droite qu'elle."
    R "Après cela, Carme et Lucien se voyaient moins. Elle érigeait un mur entre eux, car elle trouvait cela irrespectueux de continuer quoi que ce soit alors que j'étais là. Et puis..."

    B "Et puis ?"

    R "Un soir, ils se sont disputés violemment. Je ne les avais jamais vus autant en colère l'un contre l'autre. Tout le cirque a assisté à cette dispute, mais seul Zuddy en connaît la raison." 
    R "Après cela, ils ne se parlaient plus. Et cela a réellement blessé Lucien, je le sais."

    C "Et vous ne savez pas pourquoi ils se sont disputés ?"

    R "Je vous l'ai dit, seul Zuddy sait."

    C "Et pourquoi ne voulez-vous pas en parler davantage ?"

    R "Parce que cette histoire n'est pas la mienne. Si vous voulez bien, j'aimerais que l'on s'arrête là."

    $ Carmedispute = True
    jump terminerinterrof

label LucienSecrets:
    hide Rosalie_angry
    show Rosalie_serious at breathe_center
    C "Est-ce que Lucien gardait des secrets de son entourage, selon vous ?"
    
    R "Lucien aimait tout contrôler, mais il gardait certaines choses pour lui. Notamment en ce qui concernait Oliver... Il était si doux avec lui, bien plus qu'avec quiconque."
    
    C "Vous semblez hésiter, Madame Remaut. Il y a autre chose, n'est-ce pas ?"
    
    R "Lucien... il y avait quelque chose avec un autre enfant... mais je ne connais pas les détails."
    hide Rosalie_serious
    show Rosalie_regard_ailleurs at breathe_center
    
    B "Un autre enfant ?"
    
    R  "Je ne sais rien de plus. Lucien refusait catégoriquement d'en parler. Peut-être que cet enfant n'existe même pas. Ou peut-être qu'il est quelque part, en train de nous observer."
    
    B "C'est une découverte surprenante."
    
    $ knowsAboutChild = True
    menu:
        "Poursuivre sur cet enfant.":
            jump poursuivre_enfant
        "Changer de sujet.":
            jump changersujetfemme

label poursuivre_enfant:
    hide Rosalie_regard_ailleurs
    show Rosalie_serious at breathe_center
    C "Cet enfant... Vous ne savez pas qui il est ?"
    
    R "Non, et je ne l'ai jamais su. Lucien refusait catégoriquement d'en parler. Il coupait court à toute discussion à ce sujet. Peut-être que c'était une illusion, peut-être pas."

    C "Vous ne savez pas du tout ce qu'il lui est arrivé ?"

    R "Non, tout ce que je sais, c'est que cela le hantait. Mais je vous en ai déjà trop dit."

    jump changersujetfemme

label terminerinterrof:
    C "Merci pour vos réponses, madame."
    hide Rosalie
    if Carmedispute:
        B "Je suis maintenant bien curieuse de savoir pourquoi Carme et Lucien se sont disputés."
        C "Mais est-ce que ce serait assez grave au point de l'assassiner des années après ?"
    
    if knowsAboutChild:
        B "Je me demande quel âge l'enfant de Lucien doit avoir. Peut-être le connaissons-nous ?"
        C "Oui, c'est une information très importante et à ne pas négliger."

    menu:
        "Interroger Émile.":
            jump emileinterro
        "Interroger Carme.":
            jump   Carmeinterro
        "Finir par interroger Zuddy, le clown.":
            jump interroZuddy


label   Carmeinterro:
    scene scene_carme
    show Barbara at breathe_right
    show Carme at breathe_center
    show Christopher at breathe_left
    "Vous entrez dans la tente de Carme, une atmosphère apaisante et mystérieuse émane de l'endroit."
    "Des bougies allumées, des tissus colorés et des objets divinatoires ornent l'intérieur. Carme vous accueille avec un sourire doux, presque maternel."

    Carme "Bonjour. J'imagine que vous venez pour poser des questions sur Lucien ?"

    B "Oui, vous semblez avoir une longue histoire avec lui et le cirque."

    Carme "Je suis ici depuis le tout début. Lucien m'a donné un endroit que je considérais comme ma maison avec des personnes que je considère comme ma famille. "
    Carme"Je l'ai toujours respecté pour cela. Mais notre relation a changé ces dernières années."

    menu:
        "Interroger Carme sur Lucien.":
            jump LucienCarme
        "Parler de Madame Remaut.":
            jump Rosalie
        "Parler de Zuddy.":
            jump ZuddyCarme
        "Parler d'Émile.":
            jump EmileCarme

label EmileCarme:
    Carme "Émile est... un esprit torturé, je pense. Il porte un lourd passé sur ses épaules. Et pour être resté un si honnête homme, je le respecte énormément."

    menu:
        "Interroger Carme sur Lucien.":
            jump LucienCarme
        "Parler de Madame Remaut.":
            jump Rosalie
        "Parler de Zuddy.":
            jump ZuddyCarme

label ZuddyCarme:
    Carme "Zuddy est fidèle à lui-même. Il sait toujours où il va, et il protège ceux qu'il aime. Malgré ses manières parfois brusques, il reste une figure incontournable ici."
    Carme " De manière naturelle, on se tournera vers lui lorsque l'on rencontre un problème."

    menu:
        "Interroger Carme sur Lucien.":
            jump LucienCarme
        "Parler de Madame Remaut.":
            jump Rosalie
        "Parler d'Émile.":
            jump EmileCarme
label LucienCarme:
    C "Carme, vous connaissiez bien Lucien. Avez-vous remarqué des changements en lui ces derniers temps ?"
    Carme "Oh, oui... Il n'était plus le même homme. Sa passion pour le cirque s'est transformée en une obsession pour l'argent."
    Carme "C'était triste à voir. Il a perdu cette étincelle qui l'animait autrefois."
    # Pause pour la réflexion de Carme
    "Elle semble réfléchir un instant, le regard perdu dans ses souvenirs."
    Carme "Mais même avec ces changements, Lucien restait un homme fier. Trop fier peut-être..."
    "Son regard se fait plus distant, comme si elle hésitait à en dire plus."

    menu:
        "Pousser pour en savoir plus.":
            jump PousserCarme
        "Changer de sujet.":
            jump ChangerSujetCarme

label PousserCarme:
    B "Quand vous dites qu'il était trop fier, est-ce qu'il y avait quelque chose qu'il refusait de reconnaître ou de partager avec les autres ?"
    Carme "Lucien n'aimait pas montrer ses faiblesses. Même avec moi... Il y a des choses qu'il préférait garder pour lui."
    Carme " Des secrets qu'il n'a révélés à personne."
    # Pause pour la réflexion de Carme
    "Elle se fige un instant, comme si elle avait dit quelque chose qu'elle n'aurait pas dû. Mais elle reprend rapidement son calme."
    Carme "Mais cela fait partie du passé maintenant, n'est-ce pas ? Ses secrets sont désormais enterrés avec lui."
    "Barbara échange un regard avec vous, sentant qu'il y a encore plus à découvrir."

    menu:
        "Insister sr ce sujet.":
            jump Insister2
        "Changer de sujet.":
            jump ChangerSujetCarme


label Insister2:
    C "Carme, nous cherchons simplement à comprendre. Vous dites que Lucien avait des secrets."
    C "Est-ce possible que ces secrets aient un lien avec ce qui lui est arrivé ?"
    Carme "Lucien n'aimait pas montrer ses faiblesses. Même avec moi... Il y a des choses qu'il préférait garder pour lui."
    Carme "Peut-être. Mais parfois, les secrets appartiennent aux morts, et il vaut mieux les laisser en paix"
    # Pause pour la réflexion de Carme
    "Elle vous regarde avec une intensité inhabituelle, comme si elle pesait chaque mot qu'elle prononçait."
    jump ChangerSujetCarme


label Rosalie:
    C "Quels étaient les relations de madame Remaut avec le personnel du cirque et de son mari ?"

    Carme "Madame Remaut... Elle n'appartient pas au monde du cirque , c'est vrai."
    Carme " Elle et Lucien n'étaient pas faits l'un pour l'autre. Et je l'avais prévenu. Mais je n'ai jamais eu de problème avec elle."

    B "Vous n'avez jamais eu de désaccords ? Malgré le fait que vous et Lucien étiez proches ?"

    "Carme secoue la tête, un sourire paisible aux lèvres."

    Carme "Non. Elle n'a jamais tenté de me nuire, et je n'ai jamais eu de raisons de la voir comme une ennemie. Elle n'a rien à voir avec ma relation avec Lucien, c'est lui seul qui a décidé d'agir ainsi. Cependant..."

    "Carme marque une pause, semblant hésiter à poursuivre."

    Carme "Il y avait des rumeurs... que Lucien n'était pas entièrement honnête avec elle."

    menu:
        "Pousser sur les rumeurs.":
            jump PousserRumeurs
        "Changer de sujet.":
            jump ChangerSujetCarme

label PousserRumeurs:
    C "Qu'entendez-vous par 'pas entièrement honnête' ?"

    Carme "Lucien avait une vie avant elle, une vie qu'il ne partageait pas. Bien qu'il ait détruit la majorité des traces, il gardait des souvenirs de son passé."

    Carme  "Un passé qui incluait d'autres personnes. Des personnes dont il ne parlait jamais."

    B "Vous parlez d'un autre enfant, n'est-ce pas ?"

    "Carme reste silencieuse, son regard calme mais troublé puis acquiesça."
    $ knowsAboutChild = True

    menu:
        "Changer de sujet.":
            jump ChangerSujetCarme

label ChangerSujetCarme:
    C "Quand avez-vous parlé à Lucien pour la dernière fois ?"
    
    Carme "Nous nous évitions le plus possible. S'il devait me dire ou me donner quelque chose, il passait par n'importe qui d'autre."
    
    C "Que faisiez-vous le jour du meurtre ?"
    
    Carme "Comme d'habitude, je réorganisais mon travail et étudiais les étoiles."
    
    C "Selon vous, qui aurait pu le plus en vouloir à Lucien ?"
    
    Carme "Aucun nom ne me vient à l'esprit. Si j'avais des doutes sur quelqu'un, je vous l'aurais dit avec plaisir. Malheureusement, ce n'est pas le cas."

    menu:
        "Terminer l'interrogatoire.":
            jump terminerinterrocarme

label terminerinterrocarme:
    C "Merci pour vos réponses, madame."
    hide Carme with dissolve
    
    if knowsAboutChild:
        B "Je me demande quel âge l'enfant de Lucien doit avoir. Peut-être le connaissons-nous ?"
        C "Oui, c'est une information très importante et à ne pas négliger."

    menu:
        "Interroger Madame Remaut.":
            jump femmeinterro
        "Interroger Emile.":
            jump emileinterro
        "Finir par interroger Zuddy le clown.":
            jump interroZuddy

label interroZuddy:
    scene scene_zuddy with dissolve
    show Barbara at breathe_right
    stop sound fadeout 1.0
    play music "circo.mp3" fadein 1.0
    show Zuddy at breathe_center
    show Christopher at breathe_left
    Z "Alors, vous venez m'interroger aussi ? J'imagine que vous avez déjà parlé à tout le monde ici."
    
    B "Oui, nous avons discuté avec plusieurs personnes. Mais il semble que vous soyez quelqu'un de très influent dans ce cirque, Zuddy." 
    B"Peut-être avez-vous des informations que les autres n'ont pas partagées."
    
    "Zuddy esquisse un sourire sarcastique."
    hide Zuddy
    show Zuddy_smile_eyes_closed at breathe_center
    Z "Influence... Peut-être. Mais tout cela ne m'intéresse plus vraiment. Vous voulez des réponses ? Très bien, posez vos questions."


label ZuddyDialogue:
    if emileConfession is True:
        menu:
            "Demander à propos d'Émile et Rosalie.":
                jump ZuddyEmileRosalie
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre
    elif knowsAboutChild is True:
        menu:
            "Demander à propos de Lucien et son autre enfant.": 
                jump ZuddyAutreEnfant
            "Demander à propos d'Émile et Rosalie.":
                jump ZuddyEmileRosalie
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre
    else:
        menu:
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre

label ZuddyEmileRosalie:
    hide Zuddy_smile_eyes_closed
    show Zuddy_smile at breathe_center
    C "Nous avons appris que quelqu'un dans ce cirque a un faible pour Rosalie, la femme de Lucien. Émile, pour être exact. Est-ce quelque chose que vous saviez ?"
    
    "Zuddy éclate de rire, mais il n'y a aucune joie dans ce son."
    
    Z "Émile ? Bien sûr que je le savais. Ce n'est pas vraiment un secret. Le pauvre gars, on pensait tous que sa Rosalie ne lui aurait jamais accordé la moindre attention."
    
    "Zuddy secoue la tête, amusé."
    
    Z "Et pourtant, il n'a pas lâché l'affaire et il est désormais l'homme le plus probable de succéder au titre de Lucien. La belle ne va pas rester veuve longtemps."
    
    "Barbara semble pensive, tandis que Zuddy observe vos réactions avec curiosité."

    if knowsAboutChild is True:
        menu:
            "Demander à propos de Lucien et son autre enfant.":
                jump ZuddyAutreEnfant
            "Changer de sujet.":
                jump ChangerSujetZuddy
            "En savoir plus sur Rosalie.":
                jump RosalieZuddy
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre
    else:
        menu:
            "Changer de sujet.":
                jump ChangerSujetZuddy
            "En savoir plus sur Rosalie.":
                jump RosalieZuddy
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre


label RosalieZuddy:
    hide Zuddy_smile_eyes_closed
    show Zuddy at breathe_center
    B "En parlant de Rosalie. Elle n'est pas très appréciée ici, n'est-ce pas ?"
    
    Z "Non, c'est le moins qu'on puisse dire. La princesse parmi le peuple." 
    Z "Elle ne s'est jamais vraiment intégrée, et Lucien l'a mise sur un piédestal car elle lui apportait un titre."
    Z "Les autres la voient comme une étrangère, quelqu'un qui ne fait pas partie de leur monde et ne le sera jamais."
    
    C "Et vous, Zuddy ? Qu'en pensiez-vous ?"
    hide Zuddy 
    show Zuddy_eyes_closed at breathe_center
    Z "Je m'en fiche. Elle ne me dérange pas, tant qu'elle ne se met pas en travers de mon chemin. Mais je sais qu'elle n'est pas heureuse ici."
    Z "Personne ne l'était après ce mariage."

    if knowsAboutChild:  # Utilisez 'True' en majuscule, ou simplement l'expression booléenne
        menu:
            "Demander à propos de Lucien et son autre enfant.":
                jump ZuddyAutreEnfant
            "Changer de sujet.":
                jump ChangerSujetZuddy
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre
    else:
        menu:
            "Changer de sujet.":
                jump ChangerSujetZuddy
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre
label ZuddyAutreEnfant:
    hide Zuddy_smile_eyes_closed
    hide Zuddy 
    C "On nous a également dit que Lucien avait un autre enfant, un enfant dont personne ne parle. Vous êtes au courant de cette histoire, Zuddy ?"

    show Zuddy_chocked at breathe_center
    Z "Ah... vous avez entendu parler de ça, hein ? Oui, Lucien avait un fils avant Oliver. Un secret bien gardé, mais dans un cirque, rien ne reste caché très longtemps."
    
    "Zuddy croise les bras, son regard devenant plus perçant."
    hide Zuddy_chocked
    show Zuddy_smile_eyes_closed at breathe_center
    Z "Cet enfant... disons juste que Lucien ne voulait pas que son passé ressurgisse. Oliver n'a jamais été le seul héritier, mais il ne le savait même pas." 
    Z "Je suis sûr que Lucien a tout fait pour effacer cette partie de sa vie."
    
    B "Vous savez ce qui est arrivé à cet enfant ?"
    
    Z "Non. Et ça ne m'intéresse pas. Ce n'était pas mon affaire."

    if emileConfession:  # Utilisez 'True' en majuscule, ou simplement l'expression booléenne
        menu:
            "Demander à propos d'Émile et Rosalie.":
                jump ZuddyEmileRosalie
            "Changer de sujet.":
                jump ChangerSujetZuddy
            "Interroger sur le meurtre de Lucien.":
                jump ZuddyMeurtre
    menu:
        "Changer de sujet.":
            jump ChangerSujetZuddy
        "Interroger sur le meurtre de Lucien.":
            jump ZuddyMeurtre
label ZuddyMeurtre:
    C "Zuddy, où étiez-vous exactement la nuit du meurtre ?"
    
    Z "J'étais dans ma roulotte, comme je vous l'ai dit. Je préparais mon numéro, je répétais. C'est un peu ma routine. Ensuite, j'ai rejoint Émile pour un verre. On a parlé de tout et de rien, comme toujours. Nous avons discuté jusqu'à ce que le cirque s'éteigne."
    
    C "Et quand avez-vous vu Lucien pour la dernière fois ?"
    
    Z "C'était dans l'après-midi, avant que tout le monde ne commence à s'agiter pour les répétitions. Il m'a parlé brièvement... des trucs habituels. Vous savez, Lucien aimait bien donner des ordres. Il voulait que tout soit parfait. Rien de surprenant."
    
    B "Et comment décririez-vous votre relation avec Lucien ? Vous vous entendiez bien avec lui ?"
    
    Z "Lucien n'était pas du genre à avoir de véritables amis. Il respectait ceux qui faisaient le boulot, mais c'était tout. Moi, j'ai fait ma place ici à force de travail et de rires forcés. Il savait que le public m'aimait, et ça lui suffisait."
    
    C "Qu'en est-il des autres membres du cirque ? Vous avez des tensions avec quelqu'un ?"
    
    Z "Pas vraiment. Je m'entends bien avec Émile et Carme. Ils comprennent ce qu'est le cirque, ils savent ce que ça demande. Rosalie... c'est une autre histoire. Elle est là parce qu'elle a épousé Lucien, pas parce qu'elle aime ce monde. Elle se comporte comme si elle était au-dessus de tout ça."
    
    B "Donc, vous n'appréciez pas beaucoup Rosalie ?"
    
    Z "Rosalie ? Elle n'est qu'un trophée pour Lucien. Une femme de noblesse, un nom de famille. Rien de plus. Le cirque n'a jamais été son univers."
    
    C "Et Carme ? Elle semble... différente des autres."
    
    Z "Carme, c'est quelqu'un de vrai. Elle fait partie des murs du cirque, une force tranquille. On peut toujours compter sur elle, même si elle ne montre pas tout ce qu'elle ressent."
    
    B "Zuddy, vous semblez en savoir plus que la plupart des gens ici. Que pensez-vous de ce qui est arrivé à Lucien ?"
    
    Z "Ce que je pense ? Je pense que Lucien avait des ennemis partout. Il a pris des décisions qui n'ont pas toujours plu."
    
    # Le ton de l’interrogatoire devient plus tendu à ce moment, Zuddy se referme progressivement.
    
    if knowsAboutChild:
        menu:
            "Demander à propos de Lucien et son autre enfant":
                jump ZuddyAutreEnfant
    if emileConfession:
        menu:
            "Demander à propos d'Émile et Rosalie":
                jump zuddy_emilerosalie

    menu:
        "Changer de sujet":
            jump ChangerSujetZuddy


label ChangerSujetZuddy:
    C "Nous trouverons qui a fait ça, Zuddy. C'est juste une question de temps. Rien ne nous échappe."
    " Zuddy hausse les épaules, son sourire disparaît un instant"
    Z "Le temps, hein ? Vous n'en avez pas beaucoup, détective."
    
    C "Que voulez-vous dire ?"
    
    Z "La troupe va bientôt partir. Demain soir, nous lèverons le camp et ce cirque disparaîtra."
    Z "Vous n'avez qu'une journée pour résoudre cette affaire... avant que nous soyons tous loin d'ici."
    
    B "..."
    
    Z "Haha, il vaudrait mieux vous dépêcher... si vous voulez des réponses avant qu'on ne disparaisse."
    
    "Zuddy se penche légèrement en avant, yeux scintillant d'une lueur étrange."
    Z "Je sais qui l'a fait. Mais ça, c'est une information que vous ne méritez pas encore."
    
    C "Vous savez qui a tué Lucien ?"
    
    Z "Oh, je sais beaucoup de choses, détective. Mais ça... c'est pour moi. Pas pour vous."
    
    B "Attendez une minute—"
    
    Z "Je vous ai accordé assez de temps. Sortez d'ici avant que je ne change d'avis. Et n'imaginez même pas pouvoir nous retenir." 
    Z "La police a déjà clos cette enquête, et avec la réputation que vous traînez depuis votre dernière affaire, détective, vous n'arriverez jamais à les convaincre de nous retenir plus longtemps."
    
    "Un silence tombe lourdement. Barbara échange un regard avec Christopher, mais il est évident qu'ils n'ont d'autre choix."
    hide zuddy 
    hide Zuddy_chocked
    hide Zuddy_eyes_closed
    hide Zuddy_smile_eyes_closed
    hide Zuddy_smile
    "Sans un mot de plus, vous quittez la tente de Zuddy, avec une certitude troublante : il en sait bien plus qu'il ne le laisse entendre."
    
    $ zuddyKnowsCoupable = True
    
    jump start3

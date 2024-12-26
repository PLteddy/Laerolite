label mauvaise_fin:
    scene black with fade
    stop sound fadeout 1.0
    play music "pianoviolin.mp3" fadein 1.0
    
    "L'enquête n'a pas abouti. Le mystère du meurtre de Lucien Remaut restera non résolu."
    "Vous quittez le cirque avec un sentiment d'échec, sachant que le tueur est toujours en liberté."
    "Malgré tous vos efforts, certaines vérités semblent destinées à rester cachées."
    "Peut-être que certaines histoires ne sont jamais destinées à être racontées..."
    jump epilogue

label epilogue:
    scene bureau with fade
    show Barbara at right with dissolve
    show Christopher at left with dissolve

    "De retour au bureau, le silence règne. L'enquête est officiellement close."
    "Barbara regarde Christopher avec une lueur de tristesse dans les yeux."
    
    B "Je... Je dois t'avouer quelque chose."
    C "Quoi donc ?"
    B "Même si je t'en ai voulu pour... ce qui s'est passé avant, cette enquête a été différente."
    B "J'ai été vraiment contente de la faire avec toi."
    
    "Christopher se tourne vers Barbara, intrigué par ses mots."
    
    C "Pourquoi tu me dis ça maintenant ?"
    B "Parce que mes parents m'ont fiancée à quelqu'un. Je vais devoir démissionner."
    C "Démissionner ? Barbara, tu ne peux pas, tu es jeune et tu viens à peine d'arriver, tu voulais ton propre bureau!"
    
    "Barbara sourit tristement, ses yeux se posant un instant sur son bureau."
    
    B "Je n'ai pas le choix, Christopher. C'est la vie qu'ils ont choisie pour moi."
    B "Mais promets-moi une chose..."
    C "Tout ce que tu veux."
    B "Si jamais j'ai besoin de toi... viens me chercher. Peu importe où je suis."
    
    "Christopher hoche la tête, le cœur lourd."
    
    C "Je te le promets."
    
    "Barbara sourit, une larme coulant doucement sur sa joue."

    B "Être ton assistante a été les meilleures années de ma vie, tu sais."
    B "Et... il y a quelque chose que tu ignores."
    C "Quoi donc ?"
    B "Nous nous connaissons depuis plus longtemps que tu ne le penses. Mais... tu ne t'en souviens pas."
    
    "Christopher reste sans voix, tentant de comprendre ce que Barbara veut dire."
    
    "Sans un mot de plus, Barbara ramasse ses affaires et quitte le bureau, laissant Christopher seul, perdu dans ses pensées."
    hide Barbara with dissolve

    "Le silence s'installe, et Christopher réalise que cette histoire est bien plus complexe qu'il ne l'imaginait."

    "Fin."

    jump credits

label credits:
    scene black with fade

    # Optionnel : Ajouter de la musique pour les crédits
    # play music "musique_credits.mp3"

    # Texte des crédits
    $ credits_text = """
    Crédits

    Créé et codé par :
    Yussera Sebdaoui

    Art :
    Personnages - Yussera Sebdaoui

    Photos :
    Prises sur Unsplash
    Photo de :
    Ciocan Ciprian
    Giorgio Trovato
    Genny Dimitrakopoulou
    Jens Freudenau
    Richard Bell
    Eduardo Taulois
    Johnny Briggs
    Evgeni Adutskevich

    Musique :
    Prise sur Pixabay
    DSTechnician
    LAURENT BUCZEK
    Anastasia Kir
    mirkoboroni
    Lee Cander
    Andres Rodriguez

    Merci d'avoir joué !
    """

    # Afficher le texte défilant vers le haut
    show text credits_text:
        xpos 0.5
        ypos 1.0
        anchor (0.5, 1.0)
        linear 90.0 ypos -1.0  # Définit une vitesse de défilement plus lente

    # Pause pour permettre au texte de défiler complètement
    pause 250.0

    # Retour au menu principal
    return

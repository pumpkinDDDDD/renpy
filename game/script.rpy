#tes ini berubah ga dhiii YESSSSS BERUBAHHH

define K = Character ("Kid")    
define NT = Character ("Florian")
define BT = Character ("Asher")
define MD = Character ("Ms. Diascia")
define M  = Character ("Mom")
define B = Character ("Barista")
define W = Character ("Waiter")
define OK = Character ("Other Kid")
define MC = Character ("[MC]")
define LN = Character ("[LN]")
define BV = Character ("Boy with vest")   
define BJ = Character ("Boy with jacket")    
define Bo = Character ("Asher and Florian")
define ST = Character ("Stranger")

label start:

    $ NT_route = 0
    $ BT_route = 0
    
    $ MC = renpy.input("What is Your Name?")

    $ LN = renpy.input("What is your last name?")

    M "bombardilo crocodilo"

    scene oldoutside with fade
    show k happy

    K "“[MC]! [MC]! There you are! What took you so long?“"
    MC "“Sorry... I was talking to my mom.“"

    show k relaxed
    K  "“That’s okay, what matters is you’re here.“"
    show k grin
    K "“Here, take my hand! I wanna show you something!“"
    MC "“Okay! Where are we going?“"
    K "“You’ll see, close your eyes! It’ll be a surprise!“"
    MC "“Sure?“"

    scene grey with fade
    MC "“Are we there yet?“"
    K "“Nope!“"
    MC "“...“"
    MC "“Are we almost there now?“"
    K "“Nope! A little more I promise.“"
    MC "“Okay?“"
    K "“Okay, now duck and crawl here.“"
    MC "“This seems suspicious, are you sure we’re going somewhere safe?“"
    K "“I’m very sure.“"
    MC "“This is an awfully long tunnel we’re crawling through.“"
    K "“It’s fine, I cleared the way the other day so there wouldn’t be any bugs!“"
    MC "“There were bugs here?“"
    K "“Were! Past tense.“"
    K "“Anyway now careful, you can stop crawling here.“"
    MC "(!)"
    MC "(That’s quite a drop.)"
    K "“We’re almost there, just need to slip through this wall.“"
    MC "“...“"
    MC "(We’ve stopped.)"
    K "“You can open your eyes now.“"

    scene oldgreenhouse with fade
    MC "“Woahh! There’s so many flowers here!“"
    show k grin
    K "“I know right? I stumbled here by accident. I haven’t told anyone else about this place!“"
    MC "“I didn’t think we had a place like this in town...“"
    show k relaxed
    K "“So, do you like it?“"
    MC "“Yea! Thanks for bringing me here.“"
    MC "“You really haven’t told anyone else about this place?“"
    show k happy
    K "“Not a soul. This place is gonna be just for us.“"
    MC "“Promise?“"
    show k w
    "He smiles back at me in response before looking away and fidgeting around with something in his pockets for a bit. After a deep breath he finally stares back at me."
    show k relaxed
    K "“Actually, I've got something to give you.“"
    MC "“What is it?“"

    scene cg1 with fade
    MC "(His right hand disappeared into his pocket and when it emerged again, he was holding a plastic ring the shape of a flower. By the looks of it, it originally had 5 petals but broke at some point before this.)"
    K "“Uh, here. I got you this. I’m sorry that it’s missing a petal.“"
    K "“I-uhh broke it...sorry.“"
    K "“I-I can get you a new one if you don’t like this one! But you’ll have to wait for my mom to give me more pocket money.“"
    MC "“No, it’s fine I like it!“"
    K "“Really...?“"
    MC "“Uh huh! Thanks a lot!“"
    K "“Can I...put it on you?“"
    MC "“Sure!“"
    scene oldgreenhouse with fade
    MC "(I reach out my hand towards him and he gently holds it before slipping the plastic ring into my pointer finger. I’m not actually sure which one is the 'ring finger’ but maybe it is this one?)"
    MC "(Well, even if it isn’t, I’m happy to get a present anyway!)"
    show k relaxed
    K "“Here, now you’ll always have me with you in spirit.“"
    K "“If you ever miss me but I’m busy, just look at the ring and remember me.“"
    show k worried
    K "“[MC], we’ll be friends forever right?“"
    MC "“Sure! But...“"
    show k betrayed:
        linear 0.050 xoffset -10
        linear 0.050 xoffset +0
        linear 0.050 yoffset -10
        linear 0.050 yoffset +0
    K "“But..?!“"
    MC "“Mom said we’ll be moving soon, I won’t see you again for a while or...Ever?“"
    MC "“Sorry... That’s why I was late earlier.“"
    K "“[MC]...! You said you’d always stick with me!“"
    MC "“I’m sorry, I really am!“"
    K "“[MC] you liar!“"

    scene car with vpunch
    MC "(What was that..?)"
    MC "(That felt oddly familiar...)"
    M "“What’s wrong dear?“"
    MC "“It’s nothing mom! I just had a dream.“"
    M "“Good thing you woke up then, we’re almost back at our old town.“"
    MC "(Gardenville, my home sweet home until we unceremoniously had to move when I was eight.)"
    MC "(Can’t believe I’ll finally be there again after 10 years for spring break.)"
    MC "(Now that I think about it, I don't remember much about Gardenville.)"
    MC "(I guess I've tried to distance myself from it since we moved? I’ve always missed it when I think about it so I tried not to think about it at all.)"
    MC "(Now all that remains in the recesses of my mind are just faint images of my childhood memories.)"
    MC "“Mom, quick question.“"
    M "“Yes?“"
    MC "“Where are we staying again? Didn’t we sell our house?“"
    M "“Oh don’t worry about that, we’ll be staying with people you know very well.“"
    MC "(People I know very well? I don’t quite remember anyone...)"
    MC "(Who could it be...?)"
    MC "(Could it be...)"
    MC "(That kid? With the pink hair, the one that lives next door, likes to read and walk around town?)"
    MC "(Gave me a plastic ring at some point?? The ring I even brought with me here???)"
    MC "(The one I used to have a crush on?!!)"
    MC "(Shit, I don't even remember his name!)"
    MC "(Scratch that, I don’t think he ever told me his name?? Did he?? I just know his last name.)"
    MC "(Diascia, wasn’t it?)"
    MC "(...)"
    MC "(But what is his first name?...)"
    MC "(Whatever, Ms. Diascia will probably mention his name at some point in conversation.)"
    MC "(Or at least I hope so.)"
    MC "“Just to make sure, we’re talking about the Diascias right?“"
    M "“Yep, I’ve been in contact with Ms. Diascia and she has kindly agreed to let us stay.“"
    MC "“The ones who live next door and have pink hair? Has a son my age??“"
    M "“The one and only. I figured staying with them for spring break might cheer you up, no?"
    MC "“Really mom? .“"
    M "Speaking of which, we’re here!“"
    
    menu:
         "Goodie.":
             M "Can’t you be a little happier?"
             jump start2
      
         "Woo!": 
             M "That’s the spirit!"
             jump start2
            
    
label start2:
    scene outsideday with fade
    M "“Ready to go in?“"
    MC "“As ready as I’ll ever be.“"
    "sfx"
    MD "“Coming!“"
    "door opening sfx"
    MC "(After a few hurried footsteps the door finally opened and out came a beautiful middle aged woman.)"
    show md happy
    MD "“Oh! Lovely to see you two after so long. The [LN] family, yes? You used to live next door ten years ago? I believe you’ll be staying with us for spring break?“"
    M "“That’s right, good to see you haven’t changed much Diana. You seem well.“"
    MD "“Thank you, I've been as busy as ever lately.“"
    show md joking
    MD "“It was calm for a while since the boys are in college. But now trouble’s back in town.“"
    M "“I know what you mean, the house is quieter without [MC] around.“"
    MC "“Says the one who asked to call everyday.“"
    M "“I’m just joking dear.“"
    show md happy
    MD "“Anyway, why are we standing in the doorway? Come on in!“"

    scene inside with fade
    show md happy
    MD "“Welcome inside! You can put your bags over there, I'll get the boys to move your suitcases into the guest room later.“"
    MD "“I’m sure you can’t wait to meet them [MC]. After all, you used to be so close with one of them!“"
    MD "“Although I will admit, I’m not sure which one it was.”"
    MD "“They were very hard to tell apart back then, and I was so busy I barely spent time with my boys.“"
    MC "(What?? Hard to tell apart? D-does this mean that there were-)"
    MC "“I’m sorry, hold up a sec. 'One of them'? 'Boys'? As in 'Plural'??“"
    show md joking
    MD "“You didn’t know [MC]? My boys are twins.“"
    scene inside with vpunch
    MC "“WHAT???”"
    MC "“T-THEN, W-WHICH ONE DID I PLAY WITH??“"
    MC "“He never told me his name!”"
    M "“I must admit I'm also a little surprised, I thought you only had one kid.“"
    show md angry
    MD "“{b}Those boys...{/b}, they did it again.“"
    MD "“See the thing is, they used to pretend to be one person in front of strangers all the time.“"
    MD "“They've always found it funny whenever other people are confused.“"
    MD "“Which is precisely why at the very least, i had to make sure they were in seperate classes.“"
    MD "“Inside the house however, they would pretend to be each other. Telling them apart was impossible back then.“"
    MC "“What about now?“"
    show md joking
    MD "“Now? They’ve grown into their personal preferences so it is much easier to tell them apart.“"
    show md angry
    MD "“It doesn’t stop them from occasionally pretending to be each other though...“" 
    MD "“They especially love to mess with the barber.“"
    hide md
    show bt normal
    BJ "“Mom? Do we have company?“"
    MC "(!!)"
    show nt normal at left
    show bt smile at right
    BV "“I didn’t think we’d have guests.“"
    MD "“Speak of the devil.“"
    show nt sdnormal
    show bt sdglare
    "..."
    show nt questioning
    show bt smile
    BV "“Is that...[MC]?“"
    show bt chill
    BJ "“The one that used to live next door?“"
    MD "“Yes it is, now be polite and introduce yourselves. [MC] and her mother will be staying with us throughout spring break.“"
    show nt normal
    BV "“Seriously?“"
    show bt grinning
    BJ "“Sweet!“"

    show bt wink
    BT "“I’m Asher, but you already know that yea? After all, we were soo close back then?“"
    show nt happy
    NT "“Don’t kid yourself. I’m Florian, nice to see you again.“"
    show nt sdnormal
    show bt sdglare
    MC "(This does not help.)"
    MD "“So which one of you two used to play with [MC] here?“"
    show nt normal
    show bt angry
    Bo"“Me, obviously.“"
    show nt sdnormal
    show bt sdglare

    MC "(Upon hearing that, Ms. Diascia buries her head into her hand while my mom worriedly looks at me for confirmation. Unfortunately I have to silently mouth ‘no’ to her as I also don’t have any answers.)"
    show nt grin
    show bt smile
    MC "(Meanwhile, the twins relish in our confusion with smiles on their faces.)"
    show bt smirk
    BT "“Oh come on mom, it’s not our fault you used to buy us practically identical matching outfits. If you give us clothes like that, we’re gonna exploit it.“"
    show nt normal
    NT "“Even we can’t tell our clothes apart.“"
    show bt happy
    BT "“Yeaa, pretty sure we gave up and started wearing whatever.“"
    MD "“There were subtle differences.“"
    show bt smirk
    BT "“Too subtle.“"
    show nt happy
    NT "“Definitely.“"
    MD "“Come on, don’t you feel bad for [MC] here?“"
    show bt normal
    BT "“Surely [MC] can recognize which one of us it was, no? Especially since we were insperable back then?“"
    show nt normal
    NT "“For your information, it really was only one of us.“"
    show bt smirk
    BT "“The question is, which one?“"
    MD "“Boys, just tell the truth already...“"
    show bt grinning
    BT "“Nope!“"
    show nt grinning
    NT "“How about no?“"
    show nt grin
    show bt smile
    MD "“Oh come on.“"
    show md angry
    MC "(Ms. Diascia looks towards me and leans closer, whispering in my ear.)"
    MD "{size=-10}“I know my boys well enough to know when they’re telling the truth, this is one of those moments.“{/size}"
    MD "{size=-10}“It really was only of of them.“{/size}"
    MC "{size=-10}“Thanks Ms. Diascia“{/size}"
    show md smile
    MC "(Still though, the question remains. Which twin was it?)"

    MC "(Noticing my current state of confusion, Ms. Diascia opens her mouth.)"
    show md happy
    MD "“Oh I almost forgot, boys why don’t you help carry the [LN] family’s belongings into our guest room?“"
    MD "“I’m sure they could use the help.“"
    hide md
    show bt chill at right
    BT "“Sure.“"
    show nt normal at left
    NT "“Fine.“"

    scene guestroomday with fade
    show bt happy
    BT "“There you are, all done!“"
    show nt normal at left
    show bt smile at right
    NT "“You don’t need help unpacking too, do you, [MC]?“"
     
    menu:
         "I don’t knoww maybe I do?":
             show bt smirk
             BT "“In that case I’ll be happy to help.“"
             jump start3

         "No need, I’ll be fine.":
             show nt relaxed
             NT "“That’s good to hear.“"
             jump start3

label start3:
    show bt happy
    BT "“Anyway, come outside when you feel like it. I’ll take you on a short walk around town, things have changed since the last time we’re together.“"
    show nt normal
    NT "“He’s mistaken, I believe he means you and {b}I{/b}.“"
    show nt sdnormal
    show bt sdglare

    MC "“Yea okay, I still don’t know which one of you it is.“"
    show bt smirk
    BT "“Really [MC]? After all we’ve been through? You wound me.“"
    show nt normal
    NT "“To be fair, we’ve had practically zero contact since our last meeting.“"
    NT "“Take your time, I’m sure you’ll figure it out.“"
    show bt wink
    BT "“Yea we’ll give you some space for now, just remember our walk later!“"
    BT "“I’ll be waiting~“"

    show bt angry:
        linear 0.050 xoffset -10
        linear 0.050 xoffset +0
        linear 0.050 yoffset -10
        linear 0.050 yoffset +0
        repeat 2
    BT "{size=-10} “Ow! What was that for?!“{/size}"
    show nt silent
    NT "“Hmph.“"
    hide bt
    hide nt

    MC "(Those two sure are a handful, I wonder how Ms. Diascia deals with them.)"
    MC "(After stepping foot in Gardenville again for the first time in a while, I feel like my memories of this place are resurfacing.)"
    MC "(Especially the ones of{i} him{/i}...)"
    MC "(What was he like again?)"
    MC "(From what I remember he was...)"
    scene oldoutside
    
    menu:
         "Pretty quiet in front of other people.":
             MC "(I remember having to speak up for him whenever someone spoke to us, not that I mind.)" 
             $ NT_route +=1
             ST "“Ah the Diascia’s boy, how are you doing?“"
             show k neutral
             K "“...”"
             MC "“He’s doing fine.“"
             ST "“Is that your friend?”"
             show k w
             MC "“That means yes!“"
             jump start4

         "Loud and rambunctious, he really couldn’t shut up.":
             MC "(It was nice that the conversation never died down awkwardly though.)"
             $ BT_route +=1
             show k happy
             K "“[MC] ! I gotta tell you something! You won’t believe what happened!“"
             MC "“What is it? Wait, you've got another scratch!“"
             show k grin
             K "“It’s no biggie! Doesn’t hurt a bit!“"
             MC "“You sure?“"
             show k relaxed
             K "“Yea! Anyway, as I was saying...“"
             jump start4  
              
label start4:    
    scene oldinside with fade
    MC "(He’s always liked to read, we used to go to the library all the time.)"
    menu:
         "We had a blast trying out the crafts in those activity books.":
             $ BT_route +=1
             show k happy
             K "“So if I follow this, then we can have our own binoculars for our adventure!“"
             show k side
             K "“Ignoring the fact that they don’t actually work...“"
             show k relaxed
             K "“[MC] , what’re you making?“"
             MC "“I’m making our travel kit! Look here’s our passports!“"
             show k grin
             K "“Sweet! You even included my swords! You’re the best [MC]!“"
             jump start5

         "I loved hearing him read to me.":
             $ NT_route +=1
             show k relaxed
             K "“And so, Thumbelina flew on the swallow's back and arrived at a beautiful flower field. There she meets a flower-fairy prince just her size and they lived happily ever after.“"
             K "“The End.“"
             MC "“That was great! Can I get another one?“"
             show k worried
             K "“You’re not bored?“"
             MC "“Why would I be? I like hearing you talk.“"
             show k happy
             K "“Thanks [MC]!“"
             jump start5

label start5:
     MC "(And the day before I left...)"
     menu:
         "He made me a friendship bracelet.":
             $ BT_route +=1
             scene guestroomday with fade
             MC "(Now that I think about it, it was shoddily made but I like it anyway.)"
             MC"“(It has its own special place on my desk.)"
             scene oldoutside with fade
             show k relaxed
             K "“[MC] before you leave, I'd like you to have this.“"
             show k side
             K "“Uhh ignore the fact that it’s kinda falling apart at the seams.“"
             MC "“It’s okay, I’ll treasure it the same!“"
             jump start6

         "He wrote me a letter.": 
             $ NT_route +=1
             scene guestroomday with fade
             MC "(I remember that I can see some bumps on the paper, those gotta be from his tears.)"
             MC "(I still have it stored safely in my drawer.)"
             scene oldoutside with fade
             show k side
             K "“[MC] umm here.“"
             K "“Don’t open it now okay? Read it when you have time.“"
             MC "“I sure will!“"
             jump start6

label start6:
     scene guestroomday with fade
     if NT_route >= 1:
         MC "(Maybe it was Florian who I hung out with?)"
         jump start7

     else:
         MC "(Maybe it was Asher who I hung out with?)"
         jump start7

label start7:
     MC "(Then again, I won’t know for sure until I actually talk to them.)"
     MC "(Guess I gotta go on that walk with 'em first.)"
     scene inside
     MC "(When I entered the living room, I found the twins lounging on the couch. Asher was fidgeting around with pliers and chains in his hands while Florian was absorbed in his book.)"
     MC "(I don’t think either of 'em has noticed me yet.)"

     menu:
         "What are you making?":
             show bt surprised at center:
                linear 0.050 xoffset -10
                linear 0.050 xoffset +0
                linear 0.050 yoffset -10
                linear 0.050 yoffset +0
             BT "“Geez, don’t scare me like that, [MC].“"
             show bt chill
             BT "“I would’ve dropped my pliers if my grip was any looser.“"
             MC "“Sorry, you ready to go?“"
             show bt happy
             BT "“Uh huh.“"
             BT "“Florian let’s go!“"
             jump start8

         "What’re you reading?":
             show nt surprised at center:
                linear 0.050 xoffset -10
                linear 0.050 xoffset +0
                linear 0.050 yoffset -10
                linear 0.050 yoffset +0
             NT "(!!!)"
             show nt questioning
             NT "“[MC], you surprised me.“"
             MC "“Sorry, are you ready for that walk?“"
             show nt normal
             NT "“I am.“"
             NT "“Come on Asher, let’s go.“"
             jump start8

label start8:
     scene outsideday with fade
     MC "(Here I am, setting foot on Gardenville dirt once more.)"
     MC "(I didn’t get a chance to take a good look earlier but standing around the front of their house sure brings back memories.)"
     MC "(This is definitely somewhere I used to play at all the time.)"
     MC "(Makes me wonder why I’ve only found out about his twin now, especially if it really was only one of 'em that I played with.)"
     show bt happy
     BT "“Something caught your eye, [MC]?“"
     show bt smile at right
     show nt normal at left
     NT "“You’ve been spacing out for a while.“"
     MC "“Not really, it’s just been a while is all.“"
     show bt chill
     show nt silent
     BT "“It has hasn’t it? Even I haven’t seen this yard for a while.“"
     MC "“Because of college right? Your mom told me.“"
     BT "“Yea, we moved out of town for college.“"
     show nt normal
     NT "“It’s nice to finally see home after so long.“"
     show nt silent
     MC "“If you two don’t mind me asking, which college did you go to?“"
     show bt normal
     show nt normal
     Bo "“ Begonia’s Institute of Technology.“"
     MC "(!!!)"
     MC "“No WAY!“"
     MC "“I go there too!“"
     show nt questioning
     NT "“Really?“"
     show bt pleasant
     BT "“That’s nuts! What a coincidence.“"
     show nt normal
     NT "“How come we haven’t seen you around campus.“"
     
     menu: 
         "Maybe we have but we didn’t recognize each other?":
             show bt chill
             BT "“I guess it has been 10 years.“"
             jump start9
         
         "Dunno, I guess we don’t have any classes together":
             show nt happy
             NT "“That sounds reasonable.“" 
             jump start9

label start9:
     show bt smirk
     BT "“Anyway, let’s actually start heading up yea? Times a wastin’.“"
     show nt normal
     NT "“Whatever you say, although I’m willing to bet that you’re just itching for an excuse to buy a snack.“"
     show bt rolledeyes
     show nt silent
     BT "“It’s not an excuse. Isn’t this a legitimately perfect time to grab a snack?“"
     show bt smirk
     BT "“You want one don’t you, [MC]?“"

     menu: 
         "Definitely.":
             show bt wink
             BT "“I know it! My treat!“"
             jump start10

         "Not really?":
             show bt grinning
             BT "“More for me!“"
             jump start10

label start10:
     show nt normal
     NT "“I guess we’re definitely stopping by the cafe later.“"
     show bt happy
     BT "“Gotta show our guest around our favorite places!“"


     scene cafeday
     show bt grinning
     BT "“Here we are! Best cafe in town as far as I’m concerned.“"
     show bt smile at right
     show nt relaxed at left
     NT "“I can’t disagree with you there.“"
     show bt chill
     BT "“You guys want anything?“"

     menu:
         "Nope.":
             show bt normal
             BT "“Suit yourself.“"
             show nt normal
             NT "“Let’s search for a seat then.“"


             show nt normal at center
             hide bt
             NT "“Where would you like to sit, [MC]?“"
             MC "“That corner sure looks cozy.“"
             show nt happy
             NT "“I’m glad you agree, that’s my regular seat.“"
             show nt silent at left
             show b normal at right
             W "“Ash- wait no. Sorry, wrong twin. Hard to tell from behind.“"
             W "“Florian, you back in town?“"
             show nt normal
             NT "“Yes, I'll be staying here for spring break.“"
             W "“Nice, is that your partner?“"
             if NT_route >= 1:
                 show nt embarassed
             else:
                 show nt normal
                 NT "“Not at all, [MC]’s a friend.“"
                 W "“Sorry man, I thought you two seemed close.“"
                 hide b
                 show nt grinning at center
                 NT "“I suppose we are, aren’t we, [MC]?“"
                 MC "“I don’t know about that chief, I learned your name an hour ago.“"
                 show nt happy
                 NT "“You have me there.“"
                 jump start11


         "Sure":
             show nt silent
             MC "“I’ll take this one.“"
             show bt smirk
             BT "“Nice!“"
             show bt chill
             BT "“I think I'll order my regular“"
             show nt normal
             NT "“I’ll save a seat for us.“"
             hide nt
             show b normal at left
             show bt smile at right
             B "“Heyy Asher, haven’t seen you in a while.“"
             show bt smirk
             BT "“Obviously, I moved out for college remember?“"
             B "“That your partner?“"
             if BT_route >= 1:
                 show bt bangry
             else:
                 show bt normal
                 BT "“No stupid, [MC]’s a friend.“"
                 B "“My bad, you two seem pretty close.“"
                 show bt wink
                 BT "“Damn right, we are.“"
                 MC "“I wouldn’t say that, we’ve only seen each other again like an hour ago.“"
                 show bt smirk
                 BT "“Didn’t we used to play together?“"
                 show bt happy
                 BT "“You wound me, [MC].“"
                 B "“All right enough you two, here’s your drink.“"
                 show bt chill
                 BT "“Thanks man.“"
                 hide b
                 jump start11

label start11: 
     "walking sfx"
     show bt normal at right
     BT "“We’re not sitting down?“"
     show nt normal at left
     NT "“Now we are.“"
     show bt smile at right:
        parallel:
            ease .5 zoom 1.3 yalign 0.0
     show nt silent at left:
        parallel:
            ease .5 zoom 1.3 yalign 0.0
     MC "(I know they look pretty similar but when you see them side by side like this you really see their individuality seep through.)"
     MC "(Asher’s sitting like he owns the damn cafe while Florian has his legs crossed together politely.)"
     show nt sdnormal
     NT "“I feel like you visit this place too frequently.“"
     show bt sdhuh
     show nt silent
     BT "“You kiddin’?  I haven’t been here in ages.“"
     show nt sdnormal
     NT "“The waiters tend to say your name instead of mine.“"
     show bt questioning
     BT "“No way! They all know you.“"
     show nt normal
     NT "“Yes, but their first instinct seems to say that you are the one more likely to visit.“"
     show bt chill
     BT "“I guess I was here a lot.“"
     show nt grinning
     NT "“Especially back in those college entrance exam prep days.“"
     show nt grin
     show bt questioning
     BT "“Oh man, don’t even talk about those.“"
     MC "“Did you study at the cafe?“"
     show bt chill
     BT "“Errday.“"
     MC "“I feel like you’d rack up quite the bill if you bought a drink everyday.“"
     show bt happy
     BT "“Nah it's cool, they let me study here without buying anything.“"
     show nt normal
     NT "“Don’t cafes usually kick people like you out?“"
     show bt smirk
     show nt silent
     BT "“Not this cafe. Come on, most people here have known us since kindergarten.“"
     MC "“Kindergarten? How come I wasn't brought here then? I don’t remember ever being here.“"
     show nt happy
     NT "“That’s a missed opportunity, I’ll take you here again while you’re here.“"
     show bt happy
     BT "“I’ll take you to other places too, this town’s a treasure trove of places like this.“"
     MC "“Since we all got into the same college, how did you study for the entrance exam, Florian?“"
     show nt normal
     NT "“Oh I didn't need to.“"
     show bt sdangry
     BT "“Bastard got in by recommendations.“"
     show nt sdnormal
     NT "“That’s what you get for not having a certificate.“"
     show bt rolledeyes
     BT "“Yea okay, Mr. National Champion.“"
     show nt grinning
     NT "“It was nice getting a few extra weeks of vacation while you were busy studying.“"
     show bt sdangry
     BT "“Shut it jackass, this is why i didn’t wanna study at home.“"
     show nt normal
     NT "“How did you get in, [MC]?“"
     menu:
         "I got in by recommendations too.":
             show bt rolledeyes
             BT "“Oh come onnn.“"
             show nt grinning
             NT "“Welcome to the team, [MC]“"
             show bt angry
             BT "“I hate you two.“"
             jump start12

         "The entrance exams.":
             show nt happy
             NT "“I see you have a friend.“"
             show bt happy
             BT "“Damn right, glad to hear that.“"
             NT "“You two sure worked hard.“"
             jump start12

label start12:
     "Phone notif sfx"
     if BT_route >= 1:
         show nt questioning
         NT "“Oh? That’s unfortunate.“"
         show bt questioning
         BT "“What’s up?“"
         show nt normal
         NT "“I have urgent business, something about the lab report.“"
         NT "“I’ll have to return home and take care of it, see you two later.“"
         MC "“That sucks, good luck with that!“"
         show bt smirk
         BT "“See ya, dude!“"
         hide nt
         show bt smile at center:
             ease .5 zoom 1.3 yalign 0.0
         MC "“So which one of you did I play with, huh?“"
         show bt smirk
         BT "“You still haven’t figured it out?“"
         MC "“No stupid, it’s not like you two were dropping hints.“"
         MC "“‘Sides, people change a lot in ten years, no?“"
         show bt chill
         BT "“I like to think that some things stay the same no matter how much time passes.“"
         MC "“Some things do, but most don’t.“"
         MC "“What have you been up to the past ten years?“"
         show bt happy
         BT "“Nothin much, just breezing through life.“"
         MC "“What’s the story behind the piercing? I don’t remember that.“"
         show bt wink
         BT "“Felt like it, looks good yea? Made it myself.“"
         show bt happy
         BT "“I gave Florian the other side.“"
         MC "“Legit? You made it yourself?“"
         BT "“Yea, gotta keep my hands busy somehow.“"

         menu : 
             "Didn’t you make me a bracelet before I left?":
                 show bt chill
                 BT "“I did, didn’t I?“"
                 BT "“You can throw it away if it looks bad.“"
                 MC "“Nuh uh, that thing’s gonna be my family heirloom.“"
                 show bt shy
                 BT "“You kept it?“"
                 MC "“Yea? I’m not throwing away something made by a friend.“"
                 MC "(Especially when I had a crush on said friend.)"
                 show bt bchill
                 BT "“That’s... awfully nice of you.“"
                 show bt grinning
                 BT "“I’ll make you a better one I swear.“"
                 jump start13

             "Can you make one for your dear friend?":
                 show bt happy
                 BT "“I might.“"
                 BT "“We can use it to show how close we are.“"
                 MC "“Are we really?“"
                 show bt wink
                 BT "“Why not? We’re sitting together face to face, and now that Florian’s gone, it’s like we’re on a date.“"
                 MC "“Slow down there, we’ve just reunited.“"
                 show bt grinning
                 BT "“You’ve heard of ‘Slow burn’ get ready for ‘Speed Inferno’!“"
                 jump start13

         label start13:
             show bt smile
             MC "“I guess talking to you has started to stir up old memories.“"
             show bt happy
             BT "“Like going to the library? We used to do that a lot.“"
             MC "“You can say that.“"
             show bt smirk
             BT "“Speaking of the library, I gotta tell you this story.“"
             MC "“Ooh, spill.“"
             show bt happy
             BT "“Back then I went to the library like I always do yea? And when I came to borrow the book they said I already borrowed something and I can't borrow anything else until I return the previous one!“"
             MC "“Why didn’t you return the book?“"
             show bt questioning
             BT "“I didn’t have anything to return!“"
             BT "“And when I asked about it, they said I just borrowed it like 5 hours ago!“"
             BT "“And I know that’s not true because I was at the playground!“"
             MC "“Then what happened?“"
             show bt happy
             BT "“I asked them what book I borrowed and when they said it was the sixth book in a fantasy series I haven't read yet, I knew Florian was the culprit.“"
             show bt grinning
             BT "“Turns out he was using my card and pretending to be me!“"
             MC "“Really? But he seems so mild mannered.“"
             show bt smirk
             BT "“Don’t be fooled, that guy’s a little shit.“"
             show bt chill
             BT "“I’m glad he wasn’t using my library card to borrow something weird but still, I had to drag his ass back to the library so I could borrow my pick.“"
             MC "“Something weird? Like what, ‘how to commit arson 101’?“"
             show bt grinning
             BT "“Nah he’s more of a ‘how to get away with murder’ kinda guy.“"
             MC "“So what did you want to borrow?“"
             show bt happy
             BT "“It was a pattern book, I was learning to sew.“"
             BT "“Not that i’m any good at it now.“"
             show bt sdhuh
             BT "“Man would’ja look at the time.“"
             show bt happy
             BT "“We should head back before anyone worries.“"
             MC "“Let’s go then.“"
             jump start15

     else:
         show bt angry
         BT "“Aww man, the fuck?“"
         show nt sdnormal
         NT "“Is something wrong?“"
         show bt normal
         BT "“Yea, got a meeting for the exhibition prep in like 10 minutes. I guess spring break means jack shit to them.“"
         BT "“I’m gonna have to rush home, see y’all later.“"
         show bt smile
         MC "“That sucks, good luck with that!“"
         show nt normal
         NT "“Goodbye.“"
         hide bt
         show nt silent at center:
             ease .5 zoom 1.3 yalign 0.0
         MC "“So which one of you did I play with? Care to give me any hints?“"
         show nt normal
         NT "“Do you need any? I thought you would’ve figured it out by now.“"
         show nt silent
         MC "“Yes I do need them.“"
         MC "“Tell me something about yourself, what have you been up to the past 10 years?“"
         show nt normal
         NT "“The usual, I go to school, I go to the library and I study at home.“"
         show nt silent
         MC "“Awfully studious aren’t you?“"
         MC "“Got anything else in your life?“"
         show nt relaxed
         NT "“I guess I used to watch the TV with Asher, we were big ninja reptile fans.“"
         MC "“There you go, that’s something.“"
         MC "“What’s the story behind the piercing? I didn’t peg you to be the type.“"
         show nt normal
         NT "“Asher made it, he’s wearing the other pair.“"
         show nt happy
         NT "“I didn’t want to wear it at first but I suppose it is nice to have something that reminds you of home.“"
         
         menu: 
             "Like that letter you wrote me?":
                 show nt sdquestioning
                 NT "“I apologize if the letter seemed rather childish, I’m sure the paper has crumpled by now, you can throw it out if you’d like.“"
                 MC "“As if, I've kept that thing as pristine as it was when you gave it to me.“"
                 MC "“I still read it from time to time y’know? Your words will forever be immortalized in my head.“"
                 MC "(Especially because it was something from someone I had a crush on.)"
                 show nt questioning
                 NT "Did you really...?“"
                 show nt brelaxed
                 NT "“That’s.. rather embarrassing to hear.“"
                 MC "“It’s not embarrassing at all, i treasured the letter.“"
                 show nt relaxed
                 NT "“Thank you, [MC]...“"
                 jump start14

             "Maybe we should have something like that?":
                 show nt normal
                 NT "“Like what? Something matching?“"
                 MC "“Yep!“"
                 MC "(Maybe like that ring I got...? If that even is from him)"
                 show nt questioning
                 NT "“That would make it sound like we’re together, no?“"
                 MC "“Did you not claim that we were close before?“"
                 show nt brelaxed
                 NT "“I suppose I did.“"
                 jump start14

         label start14:       
             MC "“Talking to you brings back old memories y’know?“"
             show nt happy
             NT "“Does it now? I suppose we did spend a lot of time together.“"
             NT "“We used to frequent the library, did we not?“"
             MC "“We did, got any stories on that? Maybe ones after I wasn't around anymore?“"
             show nt normal
             NT "“Let’s see...“"
             NT "“I suppose there was this time Asher committed identity theft at the library.“"
             MC "“What??“"
             MC "(That’s a pretty serious word, I was looking for a lighthearted story.)"
             show nt sdangry
             NT "“He was awful.“"
             MC "“Okay, tell me about it.“"
             show nt normal
             NT "“I was rushing after classes so I could borrow the 6th ‘Miracles of Lumina’ book from the library.“"
             NT "“But when I got there, I was told I couldn't borrow the book because I hadn't returned the previous one.“"
             NT "“I was completely sure that I'd returned the previous one, so I asked them about it.“"
             show nt angry
             NT "“They claimed I had borrowed a guide on crocheting that morning, that’s when I knew it was his doing!“"
             MC "“That guy can crochet?“"
             show nt happy
             NT "“He made half of a scarf and forgot about it.“"
             show nt normal
             NT "“As it turns out he was using my library card to pretend to be me so he could borrow more books at the same time.“"
             MC "“I guess that does count as ‘identity theft’.“"
             MC "(Albeit, at a small scale.)"
             show nt happy
             NT "“I suppose I'm just glad he didn’t borrow anything weird.“"
             MC "“Like what? ‘How to commit arson 101'?“"
             show nt grinning
             NT "“I believe he’s more likely to borrow a ‘How to commit tax evasion’ book.“"
             show nt grin
             MC "“I see it.“"
             MC "“Oh shoot, it’s getting dark.“"
             show nt normal
             NT "“Would you like to return?“"
             MC "“Yea. I'd rather not stay out late.“"
             NT "“Let us be on our way then.“"
             jump start15

label start15:
     scene outsideevening with fade
     MC "“(That sure was fun.)"
     MC "(Who knew talking to an old friend or meeting a new one would be so fun?)"
     MC "(Although, the more I talk to him the more confident I am that he was the one I played with.)"
     MC "(The one that gave me the...ring.)"
     MC "(I wonder if there is a surefire way I can know. I’m pretty sure if I ask either twin they’d lie and say that they were the childhood friend.)"
     MC "(After all, if there was anything that stayed the same, it was that they liked messing with people.)"
     MC "(Maybe I can ask him about the ring?)"
     MC "(Nah, if I got the wrong twin I’m pretty, I’m pretty sure that twin will tease me to no end.)"
     MC "(And that'd be pretty hard to get over when you all live in the same house, even if just momentarily)"
     MC "(I need something really private, something only the two of us share. Something that’ll make it really clear that it was that specific twin.)"
     MC "(Something that not even his twin would know about)"
     MC "(There’s gotta be something right?)"
     if BT_route >= 1:
         show bt happy
         BT "“You’re not coming in?“"
     else :
         show nt normal
         NT "“You’re not coming in?“"
     MC "“I am, wait up.“"
     scene inside
     MC "We're back!"
     MC "(Once we entered the home, I can see that Ms. Diascia and Mom have set the table ready for dinner. The smell of the hot soup warms my heart and stomach. I feel like I’m about to start drooling.)"
     MC "“Things like this really hammer it home that I'm back, like for real.”"
     show md happy
     MD "“Just in time you two, grab a seat we’re ready for dinner.“"
    show md smile
     MC "“Oh great!“"
     M "“[MC], I made your favorite.“"
     MC "“Thanks, Mom.“"
     MC "(Man, it sure smells great)"
    show md happy
     MD "“Come sit down [MC], we've set the table for all of you already.“"
     MC "“Thankyou Ms. Diascia.“"
     MC "(I proceeded to pull out a chair right next to my mother with Ms. Diascia and those two sitting opposite from us.)"
     MD "“So where did the three of you go?“"
     hide md
     show nt silent at left
     show bt happy at right
     BT "“We took her to the best cafe in town obviously.“"
     show nt normal
     NT "“You can tell it was Asher’s idea.“"
     show bt grinning
     BT "“Nothin' like a good drink to kick off our return!“"
     MD "“I do hope you’re not constantly drinking those sugary drinks back at campus.“"
     show bt chill
     BT "“Nah, I know when to hold back.“"
     show nt sdnormal
     NT "“For some reason I don't buy that.“"
     
     menu: 
         "Me neither, you should’ve seen how fast that drink disappeared.":
             show bt questioning
             show nt grin
             BT "“Not you too, have some faith in me, why dontcha'?“"
             jump start16

         "Have some faith in him, I'm sure he’s fine.":
             show nt happy
             show bt smile
             NT "“A rare occasion, someone’s on your side."
             jump start16

label start16:            
     M "“Now now, let’s continue our dinner in peace. Shall we?“"
     MD "“Yes we shall.“"
     show bt normal
     show nt silent
     BT "“Right, sorry Ms. [LN].“"

     scene guestroomnight1 with fade
     MC "(Man, dinner was good.)"
     MC "(Honestly I can’t remember the last time I’ve had a meal on a table surrounded by people like this.)"
     MC "(Kinda nice, actually.)"
     MC "(I feel like college has ruined my eating habits a little.)"
     MC "(Now that I’ve had something in my stomach, I should probably start unpacking things.)"
     MC "(I really should've just shoved my stuff into a suitcase, i don't know why i decided to box them.)"
     MC "(Maybe I can start with that box over there?)"
     scene box with fade 
     "*rustling through stuff sfx"
     "*Enter drag and drop"
     "*If nt_route≥2 "
     "the items are an old bottle of ink, stacks of old notes, an old photo, hardcover book, journal is a standard notebook"
     "Else"
     "Items are old anatomy sketches, half of a scarf, old photo, jar of beads, journal is a sketchbook."
     "*bg is the box, makes sure all the other items cover the journal, plot only moves forward once you click on the journal, you can read the journal but in case people can’t read the writing make sure it’s also on the text box later."

     MC "(Wait a minute. This isn’t my stuff.)"
     MC "(Did I open the wrong box?)"

     if BT_route >= 1:
         MC "(Honestly, this looks more like something Asher would have.)"
         jump afterbox
     else:
         MC "(Honestly, this looks more like something Florian would have.)"
         jump afterbox

label afterbox:
     MC "(...)"
     MC "(I've got an idea.)"
     MC "(Potentially a horrible trust ruining idea but I think I need the help.)"
     MC "(If this is his journal, maybe he has mentioned me at some point?)"
     MC "(And that’ll really tell me who I played with.)"
     MC "(I mean, I already have my suspicions on which one it is but I like having irrefutable evidence at hand.)"

     if NT_route >= 1:
         show nt journal
         "Friday, X-X-XX13"
         MC "(Nice! I should still be around during this time.)"
         "Dear diary, I played with the neibor again today It was fun and it was good and they were nice to me."
         "I am very bappy."
         "I won a ring at the capsul machine, want to give to neibor"
         MC "(Aww, this is pretty cute.)"
         "Saturday, X-X-XX13"
         "I feel really angry asher broke the ring I was gonna give the neighbor (I just learned how to spell it) and it broke and now it doesn’t look good. I tried fixing it with the glue stick but it didnt work. I cant tell mom to fix it because I dont want her to know."
         "I am taking the neighbor to that place with flowers tomorrow and if I dont have money to buy another one I will have to give the neighbor the broken one."
         "Idea 1 : sell asher for money"
         "Idea 2 : sell his things for money"
         MC "(Ohh, so that’s the story behind the ring.)"
         "{u}Do not tell asher about flower place!!!{/u}"
         "Secret!!!!"
         "Update: As of XX23, Asher is still to not be told about the location."
         MC "(Aww, he’s still writing in this!)"
         MC "(And from the looks of it, he was still adding similar comments a few months ago.)"
         MC "(But also, this settles it! Florian was the one I played with! If I can make him take me to that place with the flowers, then he’ll have to drop the act and tell me the truth.)"
         MC "(Hopefully.)"
         jump start17

     else:
         show bt journal
         "Friday, XX13"
         MC "(Nice! I should still be around during this time.)"
         "Found a sick place!!!! Will show neibor later!! Has flowers and really pretty!!!!"
         "Its cool as fudge"
         MC "(Oh dear, it’s so...lame? But also incredibly endearing.)"
         "Saturday XX13"
         "I hate florian!!!!! He broke the ring for the neibor and i dont have money."
         "Have to give the neibor the broken one unless i can fix it, dont think the glue stick could work"
         "Want to try glue gun but dont have one"
         MC "(Guess that’s why the ring was broken.)"
         "Note to me: never tell him about flower place!!!!"
         "Still haven't, don’t worry lil me! -XX23-"
         MC "(Aww he still writes in this book.)"
         MC "(And looking at the other pages, there are several other recent comments from him similar to this one.)"
         MC "(But this confirms it, Asher was the one I played with as a kid! I just gotta get him to take me back to place with the flowers and that’ll prove it once and for all.)"
         MC "(Hopefully.)"
         jump start17
 
label start17:
     MD "“[MC], are you in here?“"
     MC "(!!!)"
     MC "(Shit, I gotta hide this.)"
     scene guestroomnight1
     MC "(Quickly I shove it back under the bed and hid it as best as I can. Hopefully she won’t notice that I’ve been snooping through his old belongings.)"
     MC "“I am Ms. Diascia! Wait a sec!“"
     "door opening sfx"
     show md happy
     MD "“[MC], I forgot to tell you something.“"
     MC "“What is it?“"
     MD "“I forgot to completely clear out the room before you got here, so if there are some extra boxes they’re probably the twins' old things.“"
     MD "“After all, this used to be their shared bedroom.“"
     MC "(Too late for that, I already went as far as reading their childhood journal.)"
     MC "“Oh okay, thanks for telling me.“"
     MD "“Sure thing, have a good night, [MC]. I hope you’ll enjoy your stay here.“"
     MC "“If you need anything, just call okay?.“"
     MC "“Sure thing.“"
     MC "“Goodnight Ms. Diascia.“"
     MD "“Goodnight [MC].“"
     hide md
     "*door close sfx"
     MC "(Yikes, that was close.)"
     MC "(And worse of all, all that snooping made me forget that I was supposed to unpack my all my stuff.)"
     MC "(Guess I gotta get on with it.)"

     scene guestroomnight1 with wipeleft
     MC "(Well, that covers most of it?)"
     MC "(Pretty sure the other boxes are Mom’s)"
     MC "(I stretch my arms and back from all the soreness that comes with unpacking and I look at the clock.)"
     MC "(Guess it’s that late huh? I should sleep.)"
     MC "(I share this guest room with my Mom but I guess she isn’t sleepy yet?)"
     MC "(Going up to the door, I place my ear against it to try and hear what Mom's up to. Through the door, I can hear faint laughter coming from the living room.)"
     MC "(I guess she's having a good time with Ms. Diascia)"
     MC "(Oh well, I’ll sleep first.)"

     scene guestroomnight1 with fade
     MC "( I know I said I was gonna sleep, but for some reason sleep evades me right now.)"
     
     menu:
         "I guess I’m nervous about tomorrow.":
             MC "(I know I already found definitive proof, but if I still have the wrong twin I don't think I can face them for the rest of spring break out of sheer embarrassment.)"
             MC "(I need to surprise him with it.)"
             jump start18
        
         "I’m way too excited about tomorrow.":
             MC "(I really want to pull the rug under him and surprise him with my current knowledge.)"
             MC "(He can’t fool me any longer!)"
             MC "(Just you wait, I’ll be able to call you my friend again with certainty soon enough.)"
             MC "(Or at least I will if I have the right twin.)"
             jump start18

label start18:
     scene oldoutside with fade
     if NT_route >= 1:
         show k worried
         K "“[MC]? Where are you going?“"
         MC "“Oh! My Mom told me to go with the other neighborhood kids to the playground.“"
         show k betrayed
         K "“But why? I thought we were gonna play together?“"
         MC "“I dunno either, but it might be fun once in a while, wanna come with?“"
         show k side
         K "“I-“"
         OK "“[MC]! you coming?“"
         MC "“Wait a sec!“"
         "Before I can turn around to face him again, I feel his head on my back. He grips the side of my shirt and with a low and quiet voice he starts..."
         show k worried
         K "“[MC]...“"
         MC "“What is it? Are you okay?“"
         K "“I think I’m sick.“"
         MC "“Oh no! That’s not good.“"
         K "“Can you stay with me until my mom gets back? Please...?“"
         MC "“I guess I can't leave you alone can I?“"
         MC "“Sorry guys I can’t come! I’m gonna stay with him instead.“"
         OK "“Okay! Bye, [MC]!“"
         MC "“Bye!“"

         scene oldinside with fade
         MC "“There we go! You’re all cozy now.“"
         show k relaxed
         K "“Thank you, [MC]?“"
         MC "“Do you need any medicine?“"
         K "“Nope, I just need you to stay with me.“"
         MC "“Okay.“"
         K "“...”"
         MC "“What are you sick with anyway? You were fine earlier.“"
         show k side
         K "{size=-10}“...that’s because I’m just pretending so you wouldn’t go.“{/size}"
         MC "“What was that? Sorry, couldn’t hear you.“"
         show k relaxed
         K "“I-I don’t know either but I’m sure I’ll get better soon.“"
         MC "“Okay then!“"
         K "“Just...stay with me until mom gets back okay, [MC]?“"
         MC "“Don’t worry, I’ll stick with you.“"
         jump start19

     else:
        
         show k grin
         K "“[MC]!“"
         MC "“What is it? I’m about to leave.“"
         show k worried
         K "“Leave? Leave where?! Aren’t you gonna hang out with me?“"
         MC "“Oh! My Mom told me to go with the other neighborhood kids to the playground.“"
         show k grin
         K "“Oh okay, I'll go to Jacob’s house then. Have fun but remember to play with me later!!“"
         MC "“Okay! Byee!!“"
         K "“See you later, [MC]!!“"
         scene oldinside with fade
         MC "“Heyy!! I’m here now!!“"
         MC "“...”"
         MC "(He’s not answering.)"
         show k worried
         K "“[MC]?“"
         MC "“I’m here to play with you now!“"
         K "“But it’s getting late now, are you sure?“"
         MC "“Yep! I live next door anyway.“"
         show k relaxed
         K "“Okay...Did you have fun earlier?“"
         MC "“uh huh.“"
         show k happy
         K "“But I’m still number 1 yea? You won’t leave me right? You’ll still come back and play with me?“"
         MC "“Of course!“"
         show k relaxed
         K "“That’s...good.“"
         MC "“Quick question, what’s all the tissues on the table from? Did you spill something?“"
         show k side
         K "“Ignore that, I forgot to clean up. I'll do it now“"
         show k neutral
         MC "“Actually, your eyes are red! Did you cry...?“"
         show k side
         K "“No...“"
         MC "“You’re lying!! You were, that’s why your pants are on fire now.“"
         show k betrayed
         K "“No they’re not, stupid.“"
         MC "“You wanted to play with me so bad!“"
         show k worried
         K "“No...“"
         MC "“I thought you played with Jacob?“"
         show k relaxed
         K "“I did, but I like you more.“"
         MC "“Really?“"
         show k side
         K "“Maybe...“"
         MC "“That’s okay you can play with me now!“"
         show k relaxed
         MC "“I’ll always stick with you!“"
         jump start19

label start19:
     scene guestroomday with fade
     scene grey with fade
     scene guestroomday with fade
     scene grey with fade
     scene guestroomday with fade
     scene grey with fade
     MC "(What...was that?)"
     MC "(Huh.)"
     MC "(I guess being back at Gardenville brings back more memories than I thought.)"
     MC "(I’m still having dreams about him.)"
     MC "(Guess that’s what he did back then, I wonder if he’ll still have a similar reaction?)"
     MC "(Hmm, that’s what I’ll have to find out today.)"

     scene inside with fade
     MC "“Mornin'.“"
     show bt grinning
     BT "“Mornin’!“"
     show nt normal at left
     show bt smile at right
     NT "“Good morning, [MC].“"
     show nt silent
     M "“You’re up pretty early, [MC]. I thought you would sleep in since it’s spring break.“"
     MC "“I guess I couldn't continue sleeping, I had a dream.“"
     show bt smirk
     BT "“Is it of me?“"
     show nt happy
     NT "“Must be a nightmare then.“"
     show bt sdangry
     BT "“Hey!“"
     show nt grinning
     NT "“If it was of me on the other hand-“"
     show bt smirk
     show nt sdnormal
     BT "“Then it’d be even worse!“"
     
     menu:
         "It is related to one of you actually.":
             show bt grinning
             BT "“See I was right!“"
             show nt happy
             show bt sdglare
             NT "“One of us. It might not be you.“"
             jump start20
         
         "I don’t knoww.":
             show bt grinning
             BT "“Come onn, don’t keep me guesin’!“"
             show nt normal
             NT "“Shut up already.“"
             jump start20

label start20:
     show nt silent
     show bt smile
     hide bt
     hide nt
     show md joking
     MD "“Boys, please have your breakfast in peace.“"
     MD "“I’m sure [MC] will get a headache if you keep bantering this early.“"
     show md happy
     MD "“Anything you’d like, [MC]?“"
     
     menu: 
         "Can I get some cereal?":
             MD "“Coming right up!“"
             jump start21
         
         "Toast would be nice.":
             MD "“Here you go!“"
             jump start21
         
         "I can get it myself.":
             MD "“Okay then!“"
             jump start21
         
         "No need.":
             MD "“Okay, call me if you need anything.“"
             jump start21

label start21:
     scene inside with fade
     MC "(Is the coast clear? Any one that can disturb my plans?)"
     MC "(Ms. Diascia and Mom left earlier for a little ‘Mom Hangout’ at the nearby mall, so there shouldn’t be anyone else in the house.)"
     MC "(Now that the mornings practically done, I can get on with my actual plan for today.)"
     MC "(Where is he?)"
     MC "(Oh, there he is. There’s no one else around him right?)"
     MC "(I don’t see his twin, it’s go time.)"

     if NT_route >= 1:
         MC "“Whatcha doin'?“"
         show nt surprised
         NT "(!)"
         show nt questioning
         NT "“[MC]...You need to stop surprising me like this.“"
         show nt silent
         MC "“Sorry, I'll stop.“"
         MC "“But really, what are you doing today?“"
         show nt normal
         NT "“well not much, but I’m planning on picking up writing during break.“"
         NT "“Then maybe, I'll study ahead for midterms later.“"
         MC "(Yikes, I forgot we had those.)"
         show nt happy
         NT "“Anyway, if you’re striking up a conversation with me, I can only assume that you’ve taken interest in me. So, what are you doing today, [MC]?“"
         MC "“Oh you know, nothing much. But I was thinking of going around town with Asher later, he did say the town is a treasure trove of cool places.“"
         show nt questioning
         NT "“What?“"
         MC "“Yea, I'm planning on it being just the two of us.“"
         MC "“Especially since I already spent time yesterday with you.“"
         MC "“Or I might visit the other neighbors, I think 10 years away from here is enough for a reunion, no?“"
         show nt sdquestioning
         NT "“But, [MC] I-I...“"
         MC "(There we go, the cracks are starting to show.)"
         MC "“But what?“"
         NT "“I..I...“"
         MC "“What is it?“"
         show nt sick:
            parallel:
                ease .5 zoom 2.0
            parallel:
                yalign 0.0
                linear 0.0 yalign 0.0 xalign 0.5
         MC "(Suddenly his head falls to my shoulders and he starts to grip the sleeves of my shirt. He's not holding it too tightly but it’s noticeable enough that I'd feel bad if I moved away.)"
         MC "(He’s so close I can hear him breathing and with a low quiet voice he lets out...)"
         show nt brelaxed
         NT "[MC]...Can you please stay like this for a while? I..I think I'm sick.“"
         MC "(Bingo! He’s still pulling out the sick card.)"
         MC "“Yea I can, are you okay?“"
         MC "(I know damn well he’s okay.)"
         NT "“Not really? I don’t feel-“"
         show nt sdnormal at left:
             ease .5 zoom 2.0 yalign 0.0
         show bt happy at right
         BT "“Yo! What are you two doing?“"

         MC "“Florian’s sick apparently.“"
         show bt wink
         BT "“{i}Sick{/i}, huh?“"
         MC "(Oh, he knows all right.)"
         show nt normal
         NT "“Yes I am.“"
         BT "“I don’t knowww, you seemed fine earlier.“"
         NT "“Well that was earlier.“"
         show bt smirk
         BT "{i}“Oh no, my poor twin, whatever shall I do when you’re terribly ill?“{/i}"
         show nt sdangry
         show bt smile
         NT "“Asher...“"
         MC "(He’s completely fooling around by this point.)"
         MC "(When Asher eventually looks at me, my expression must’ve given me away because he soon gives me a knowing smirk as if to say ‘I gotchu dude!’.)"
         show bt wink
         BT "“Say [MC], let’s go out on the town together. Just the two of us.“"
         show bt smirk
         BT "“Y’know while Florian’s sick and all.“"
         BT "“The medicine’s on the top shelf if he needs any.“"
         BT "“Whaddya say, [MC]?“"
         show nt surprised
         show bt smile
         MC "“Hmm, that’s a tempting offer.“"
         show nt questioning
         NT "“But, [MC]...“"
         show nt sick
         MC "“His grip on my sleeves starts to tighten and I can faintly hear him grumble under his breath.“"
         MC "“Actually, I'm afraid I'll have to change my mind. I’ll stay here and take care of Florian.“"
         show bt smirk
         BT "{i}“Oh my! You worry so much about him! Maybe I'll also stay home and help you nurse him back to health.“{/i}"
         BT "“I can’t leave you two {i}alone{/i} together.“"
         show nt sdangry
         show bt smile
         MC "(For a brief moment Florian seems to forget that I’m right next to him and I can see him quietly mouth ‘fuck you’ to Asher, this action doesn’t seem to affect Asher as his smirk seems to only get more annoying.)"
         show bt smirk
         BT "“Oh wait, I don’t have to worry do I?“"
         BT "“[MC]’s right there to take care of you, yea?“"
         BT "“I’ll just...go around town and leave you two all alone.“"
         show bt wink
         BT "“See y'all!“"
         "*door closed sfx"
         hide bt
         show nt silent at center
         MC "(I’m glad he caught on so quickly, now it’s just me and him in the house.)"
         MC "“So would you like to lay down?“"
         show nt sick
         NT "“Yes please.“"
         MC "“Alright then, do you want anything else? Some medicine perhaps?“"
         NT "“Can you...Stroke my head?“"
         MC "“Sure...“"
         show nt relaxed
         NT "“Thank you [MC], this feels...“"
         NT "“..nice.“"
         show nt grin
         MC "“Glad to hear that“"
         MC "“Although...You’re not really sick, are you?“"
         show nt embarassed
         NT "(!!)"
         show nt questioning
         NT "“What makes you think that, [MC]?“"
         MC "“You don’t really change your modus operandi, you used to do the exact same thing back then!“"
         MC "“Remember how you used to pretend to be sick just so I don’t play with other kids?“"
         show nt sdquestioning
         NT "“I didn’t...“"
         MC "“But you did, after all {b}you{/b} are the one I played with aren’t you, Florian?“"
         NT "“What makes you think that?“"
         MC "“Well I had my suspicions yesterday, but the whole ‘sick act’ thing really sealed the deal for me.“"
         MC "“So? Any rebuttals?“"
         show nt silent
         NT "“...”"
         show nt questioning
         NT "“Well, you have me there...“"
         MC "“You’re not lying this time, right?“"
         show nt normal
         NT "“No? But to be fair, any liar can just say that.“"
         NT "“I wonder what i can do to prove it to you“"
         MC "“I know how you can prove it.“"
         NT "“How...?“"
         MC "“Take me back to the place with all the flowers, the one you showed me the day I told you I was moving.“"
         show nt brelaxed
         NT "“You still remembered?“"
         MC "“I never forgot!“"
         show nt normal
         NT "“Let me take you there, right now.“"
         MC "“I’m not closing my eyes this time.“"
         show nt grin
         MC "(He responds with a grin, as cheeky as the Cheshire cat and he takes my hand and leads me outside the house.)"
         scene outsideday
         MC "(We went past all the other houses in the neighborhood, past the old playground we used to go to, past our elementary school and eventually, to the north wing of the park.)"
         MC "(He takes me through several bushes and an overgrown path which eventually lead to a pipe big enough for a human to crawl through and after squeezing through a brick wall, we made it.)"

         scene greenhouse with fade
         MC "(So it was here.)"
         MC "(It hasn’t been any last magnificent as I’ve last seen it in my memories.)"
         MC "“So, where are we?“"
         show nt normal
         NT "“Gardenville Museum’s Greenhouse or what’s left of it.“"
         MC "“We’re allowed here, right?“"
         show nt grin
         NT "“...”"
         MC "“Oh no, that’s not good.“"
         show nt grinning
         NT "“Well it’s nothing punishable by law, probably.“"
         MC "“That’s not very reassuring, how did you find this place anyway?“"
         show nt happy
         NT "“Nothing major, I simply went on my very own little journey during our field trip to the museum.“"
         MC "“Seriously? I went ages looking for you back then.“"
         show nt relaxed
         NT "“I believe I apologized for that, did I not? We even walked home together.“"
         MC "“I guess you did.“"
         show nt normal
         NT "“Straying off topic, I have a question for you.“"
         MC "“Shoot.“"
         show nt sdquestioning
         NT "“Remember the ring I gave you? Do you...still regard me as your friend? Even after all these years?“"
         NT "“I’ve thought of contacting you all this time but I never knew how, after all I forgot to ask for your new address. I couldn’t send you a letter.“"
         NT "“I was afraid asking my mother may bring unwanted questions so I suppose I never asked.“"
         NT "“I did try to distract myself from thinking about you by studying but that didn’t bring the effects I wanted.“"
         NT "“You still remain as a constant thought in my mind all this time.“"
         NT "“So, what I'm trying to say is...“"
         show nt brelaxed
         NT "“I had a crush on you back when we were children, I suppose you must’ve noticed by the way I pretend to be sick whenever someone is stealing you away from me.“"
         NT "“You were always so patient with me, you’ve always spoken up for me when I had trouble doing so.“"
         NT "“You listen to what I say even when I'm sure it must’ve been quite boring and you seem to entertain my selfish little whims.“"
         NT "“Now that you have returned, I can confirm that those feelings I've had were not misplaced.“"
         NT "“I...love you.“"
         MC "(After all this time, he still...Damn it, I guess I also still love him.)"
         show nt happy
         NT "“[MC], I see the way you are staring at me. I believe your expression means something positive, no?“"
         NT "“If you’d like to kiss me there is no need for such pretenses. You may do it whenever the mood strikes you.“"
         MC "“You sure are forward with it.“"
         show nt grinning
         NT "“Am I mistaken in my assumption?“"
         MC "“Not at all.“"
         scene grey with fade
         "With that, I draw him into a kiss as gentle as it is passionate. I find my hands grabbing him by the waist while his hands roam around my back."
         "In that slight moment, it feels like all time has stopped. It was only when we started running out of breath did we remember to breathe again."
         scene greenhouse with fade
         show nt brelaxed:
            parallel:
                ease .5 zoom 2.0
            parallel:
                yalign 0.0
                linear 0.0 yalign 0.0 xalign 0.5
         NT "“[MC]...“"
         show nt embarassed
         MC "“Here, I still have the ring.“"
         NT "“You kept it...“"
         MC "“I did.“"
         scene ntcg with fade
         NT "“Is it safe to assume-“"
         MC "“That we’re dating and I love you back? Yes.“"
         NT "“That’s...Pleasant to hear.“"
         NT "“Say it again.“"
         MC "“I love you?“"
         NT "“Again.“"
         MC "“Okay, slow down there.“"
         NT "“No, say it again. Please?“"
         MC "“What do I need to get you to stop?“"
         NT "“I will once my lips are occupied.“"
         MC "“You cheeky brat.“"
         NT "“And yet, you are still fond of me, no?“"
         MC "“Against all odds, I am.“"
         NT "“Now that we are together, I have something else to say.“"
         MC "“What is it?“"
         NT "“I’m afraid I may be more possessive than I ever thought, I find myself wanting you all to myself.“"
         NT "“[MC], can I be presumptuous enough to believe you will no longer leave my side?“"
         MC "“Yes you can.“"
         NT "“Prove it.“"
         MC "“With what? I feel like this is just another way to get me to kiss you again.“"
         NT "“Is it not working?“"
         MC "“Hmm...“"
         MC "“Unfortunately for me, it’s working a little too well.“"
         MC "“Come here.“"
         NT "“Hmph-“"
         MC "(With that, our lips united once more as we embraced amongst the flowers, sealing our relationship into a blossoming mutual agreement.)"
         MC "(Despite our years apart, our bond seemingly hasn't wavered in the slightest as it remained as strong as an iron wall. If being apart only made us grow stronger, I don't see a future where we’ll ever be apart again.)"
         "THE END : 'Florian's Route"

     else:
         MC "“What are you doing?“"
         show bt surprised at center:
            linear 0.050 xoffset -10
            linear 0.050 xoffset +0
            linear 0.050 yoffset -10
            linear 0.050 yoffset +0
         BT "(!)"
         show bt questioning
         BT "“Geez, ya gotta stop spookin’ me like that.“" 
         MC "“My bad.“"
         MC "“But really, what are you doing today?“"
         show bt happy
         BT "“Oh, I’m planning on starting on my projects for class.“"
         show bt questioning
         BT "“Can you believe I have to lug around that giant bag back home? It’s insane how big they want us to make these things.“"
         show bt happy
         BT "“Enough about me though, what are you doing?“"
         show bt smirk
         BT "“Although judging by the fact that you’re approaching me, I'm guessing you wanna hang out with me?“"
         MC "(It’s go time.)"
         MC "“Nah actually I’m planning on going with Florian instead, he said he was gonna take me to that cafe again since he left early yesterday.“"
         show bt normal
         BT "“Oh.“"
         show bt chill
         BT "“I can join you two?“"
         MC "“Nah, we already spent a long time in the cafe yesterday.“"
         show bt happy
         BT "“Well in that case, have fun! I’ll be back here if you need me.“"
         show bt sdglare at right
         show nt normal at left
         NT "“[MC]? What are you doing?“"
         MC "(Oh shit, the real guys here!)"
         show nt surprised
         MC "There you are, I was waiting for you, let's go!“"
         show nt grin
         MC "(I give him a pleading glance, I'm just hoping he understands and goes along with it. He’s seemingly confused for a moment until he looks over at Asher and his lips curl up into the smallest little grin.)"
         show nt happy
         NT "“My apologies, [MC]. Sorry for my tardiness. Let’s go shall we?“"
         MC "“Yes, let's go.“"
         show nt grinning
         NT "“Be nice and guard the house while {i}I{/i} go with [MC] okay?“"
         show bt rolledeyes
         BT "Yea, yea whatever.“"

         scene outsideday with fade
         MC "“Thanks for playing along.“"
         show nt normal
         NT "“So what are you planning?“"
         MC "“Before I answer that, I've got a quick question.“"
         NT "“Go ahead.“"
         MC "“Tell me a spot in town with lots of flowers and a waterfall.“"
         NT "“There’s a place like that in town?“"
         show nt silent
         MC "“I check his expression for any hints of a lie but his face remains as neutral as always, I can't seem to find any falsehoods in his words.“"
         MC "“Don’t lie to me, if you know then spill.“"
         show nt normal
         NT "“I’m not aware of the location, if anything that seems more like Asher’s spot. You might want to ask him.“"
         MC "“Alright then, that tells me all I need.“"
         show nt happy
         NT "“I believe it’s time you answer my question, no?“"
         MC "“I’m getting to it. So y’know how some people say they’re cool with something but then they sulk about it later?“"
         show nt sdnormal
         NT "“Sounds like the sort of stupid thing Asher does.“"
         MC "“Precisely!“"
         show nt grinning
         NT "“I see what you’re planning now.“"
         MC "“He used to do it back then, I figured he’d do something similar now.“"
         show nt happy
         NT "“Good thing he still does.“"
         show nt grinning
         NT "“If you want to peek at his reactions, try that window over there. He’s never been good at hiding for long, you’ll start hearing him grumble soon enough.“"
         MC "“Thanks man, you’re surprisingly helpful, y’know that?“"
         show nt questioning
         NT "“Surprisingly?“"
         MC "“Never mind, thanks for the help.“"
         show nt normal
         NT "“Sure thing, I'll be at the library if you need me.“"
         MC "(Moment of truth.)"

         scene inside with fade
         show bvn window
         show bt angry
         BT "{size=-7} “Stupid [MC]...goin’ out with Florian instead, hmph!“{/size}"
         BT "{size=-7}“Even though it was me you played with...“{/size}"
         BT "{size=-7}“Whatever, I guess I'll just start sketchin’ while they’re gone.“{/size}"
         BT "{size=-7}“Stupid [MC]...Should’ve been with me.“{/size}"
         MC "“What was that?“"
         show bt bangry
         BT "(!!!)"
         BT "“[MC] what the fuck?? You really gotta stop that y’know?“"
         MC "“My baddd.“"
         BT "“You sure don’t look like you feel bad about it, where’s Florian anyway?“"
         BT "“Thought you were going out with him.“"
         MC "“Changed my mind! And more importantly...I heard that!“"
         show bt angry
         BT "“Heard what?“"
         MC "“Everything you said. Starting from 'Stupid [MC]' and 'It was me you played with...!' and every other thing you said.“"
         show bt bangry
         BT "“I do not sound like that!“"
         MC "“Yea you do.“"
         show bt surprised
         MC "“Actually wait a minute, let me climb through the window here.“"
         show bt questioning
         BT "“The doors right there!“"
         MC "“I know, but this is faster.“"
         "*thump sfx"
         scene inside with vpunch
         show bt surprised
         MC "“Anyway, back on topic. You can’t fool me anymore, I know it was you who I played with!“"
         show bt bangry
         BT "“You just said that because you heard me say it!“"
         MC "“Nope, I had my suspicions yesterday and your actions today proved it!“"
         MC "“What you said just sealed the deal.“"
         show bt questioning
         BT "“Huh? What did I do that gave it away?“"
         MC "“That! Y’know, the way you get all huffy if I play with someone else even though you told me to have fun earlier!“"
         MC "“You used to do that too back then.“"
         show bt bangry
         BT "“That’s barely proof!“"
         MC "“I know what else can be proof.“"
         MC "“Take me to that place again, the one with all the flowers and the waterfall.“"
         MC "“The one you took me to the day I told you I was moving.“"
         show bt shy
         BT "“You still remember?“"
         MC "“I never forgot.“"
         BT "“[MC]...you...“"
         show bt bangry
         BT "“Aw shit, I'm getting sentimental.“"
         MC "“You can cry if you want?“"
         show bt smirk
         BT "“No, not yet. I can’t take you there if I can't see the way.“"
         BT "“Let’s go.“"
         MC "“I don’t have to close my eyes this time, right?“"
         show bt smile
         MC "(No words were spoken, but something tells me that his smirk says it all.)"

         scene outsideday with fade
         MC "(He grabs my hand and leads me outside the house, past all the other houses in the neighborhood, past the old playground we used to go to, past our elementary school and eventually, to the north wing of the park.)"
         MC "(He takes me through several bushes and an overgrown path which eventually lead to a pipe big enough for a human to crawl through and after squeezing through a brick wall, we made it.)"

         scene greenhouse with fade
         MC "(So it was here.)"
         MC "(It hasn’t been any less magnificent as I’ve last seen it in my memories.)"
         MC "“So, where are we?“"
         show bt chill
         BT "“Gardenville Museum’s failed ex-greenhouse and botany exhibition.“"
         MC "“What? Are we allowed in here?“"
         show bt smirk
         BT "“This place used to cost actual tickets to go in, now it’s free.“"
         MC "“But are we allowed in here?“"
         show bt sdhuh
         BT "“Umm...good question, I don’t know.“"
         show bt questioning
         BT "“But no one else is ever in here! Besides, the place shut down a decade before we were born.“"
         MC "“How did you find this place anyway?“"
         show bt happy
         BT "“Snuck out during our field trip to the museum.“"
         MC "“No way! No wonder I couldn't find you. I searched the whole museum back then.“"
         show bt sdhuh
         BT "“Sorry about that.“"
         show bt grinning
         BT "“But we still ended up walking home together, didn't we?“"
         MC "“I guess we did.“"
         show bt shy
         BT "“Anyway...umm can...I say something?“"
         MC "“What is it?“"
         BT "“Remember when I gave you a ring back then?“"
         MC "“Yea?“"
         BT "“Are we still...friends forever? Like, did you ever miss me?“"
         BT "“Cause’ I missed you, but I couldn’t contact you at all.“"
         BT "“I didn’t have your number, and I guess I was too embarrassed to ask my Mom for it.“"
         BT "“And since you didn’t contact me, I figured you forgot about me.“" 
         BT "“So I tried forgetting about you but I just couldn’t, and now that you’re back it feels...“"
         BT "“Everything I've been holding back just bursted out and now I can't stop saying stupid shit in front of you.“"
         show bt bangry
         BT "“Fuck.“"
         BT "“Y’know what, feel free to forget about all this later but hear me out!“"
         BT "“I had a crush on you back then! And when I look at you now...I...I feel like the crush hasn’t stopped.“"
         show bt bchill
         BT "“You’ve always been too nice to me.“"
         BT "“You pay attention to what I like and what I don't, you go along with all the stupid things I do even when you said it was stupid.“"
         show bt shy
         BT "“You’re nice to talk to and I just...I...I...“"
         BT "“I still love you, [MC].“"
         BT "“Now I get it if you...“"
         MC "“Asher, shut the fuck up.“"
         show bt betrayed
         BT "“What?“"
         MC "“Can I kiss you?“"
         show bt bchill
         BT "“Yes pleas-“"
          
         scene grey with fade
         MC "(Without a moment to spare I pull him deep into a kiss, my right hand holding him by the waist and my left buried in his hair. He responds by flinging his arms over my shoulders and embracing me as we dive further into each other's warmth.)"
         MC "(Only once we ran out of breath do we finally pull apart.)"

         scene greenhouse with fade
         show bt shy:
            parallel:
                ease .5 zoom 2.0
            parallel:
                yalign 0.0
                linear 0.0 yalign 0.0 xalign 0.5
         BT "“[MC]...“"
         MC "“I still have the ring by the way.“"
         MC "“Look.“"
         scene btcg with fade
         "As I pull out the cheap plastic ring out of my pockets, I can see his eyes shine with a mix of delight, surprise and maybe even the slightest threat of tears."
         BT "“Does this mean...?“"
         MC "“It’s my turn to say it, I love you too.“"
         BT "“So are we-“"
         MC "“Yes, we’re dating now.“"
         BT "“[MC], how do you know what I’m about to say?“"
         MC "“Because I love you.“"
         BT "“Stopp, it’s getting embarrassing.“"
         MC "“I love you~“"
         BT "“[MC]...“"
         MC "“C’mon, you’re the one who gave me a ring. It’s like you wanted to skip dating and go straight to marriage.“"
         BT "“I...I...“"
         BT "“I guess...“"
         MC "“Don’t look away from me now.“"
         BT "“I’ve got nowhere to run, do I?“"
         MC "“Nope!“"
         BT "“Well it’s not like I wanted to anyway. I’ve loved you for more than half my life and it’s too late to stop now.“"
         scene grey with fade
         MC "(And with one last kiss, we sealed the deal on our relationship. From simple childhood friends our feelings have blossomed into a romance I'll never forget.)"
         MC "(I don’t quite know what the future has in store for us, but I'm sure if 10 years of separation isn’t enough to pull us apart then nothing will.)"
         "THE END : Asher's Route"

# bang, endingnya kalau bisa kita coba ada transisi fade biar ga lgsg abrupt kaya si gr




    



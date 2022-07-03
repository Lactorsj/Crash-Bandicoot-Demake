# Crash Bandicoot Demake by Team Sparrow

a Group Project of Hebut &amp; University-365 Students from Team Sparrow
![Sparrow Logo](https://i-s2.328888.xyz/2022/06/29/62bc68d9c4c00.png)



---
## How to play?

Just type `python main.py` in your command line.

---
## Design Preview
### Visual Intent

![start.png](https://s1.328888.xyz/2022/07/03/0DJC.png)

### Visual Reference

You can modify the picture in the `\code\Assets\images` to customize the game for yourself!

1. The OBJECTS
    1. Basic crate: code\Assets\images\boxes\BasicCrate.png

        - The basic crate contains a small number of Wumpa fruit.

    2.  Bounce crate: code\Assets\images\boxes\bigcrate.png

        - The bouncing crate contains 10 Wumpa fruits and you must jump on the box to get them back.

    3. Arrow crate: code\Assets\images\boxes\boxFleche.png
    
        - The arrow crate allows Crash Bandicoot to jump higher (often to reach other boxes). It can only be destroyed with a tornado attack.
    
    4. Aku Aku crate: code\Assets\images\boxes\boxAku.png
    
        - The Aku Aku crate allows Aku Aku to level up (one more feather).

    5. Crash crate: code\Assets\images\boxes\boxCrash.png

        - The Crash crate allows Crash Bandicoot to recover an additional life directly.

    6. Iron crate: code\Assets\images\boxes\boxAcier.png
    
        - The iron crate cannot be destroyed.
    
    7. TNT crate: code\Assets\images\boxes\boxTNT.png
    
        - The TNT crate explodes if you make a spin attack. If you jump on the TNT crate, a 3-second timer is triggered, and the crate explodes at the end of it.
    
    8. Nitro crate: code\Assets\images\boxes\boxNitro.png
    
        - The Nitro crate explodes at the slightest contact, whether with a jump or a spin attack.
    
    9. Wumpa fruit: code\Assets\images\boxes\wumpa.png
    
        - The Wumpa fruit is an object to be recovered all along the level. If Crash Bandicoot manages to collect 100 Wumpa fruits, he earns an extra life in exchange for his last ones.


2.  HAZARDS

    1. Hole: code\Assets\images\obstacles\fire.png
    
        - The hole forces Crash Bandicoot to jump to avoid instant death.
    
    2. Water: code\Assets\images\obstacles\water.png
    
        - The water is like a hole and forces Crash Bandicoot to jump to avoid instant death. The difference is that it can have enemies like fish.
    
    3. Spiked pillar: code\Assets\images\obstacles\spikePillar.png
    
        - The spiked pillar is hidden in the ground and comes out at regular intervals.
    
    4. Flame : code\Assets\images\obstacles\fire.png
    
        - Fire is a platform that Crash Bandicoot must use to continue. The principle of fire is that it alternates between an on and off state, each state lasts a few seconds.


3. The ENNEMIES 

    1. Crab: code\Assets\images\ennemies\crab.png

        - The crab has no attack, it just moves over a small area of the map. If you jump on it; you take a damage. You can kill him by making the spin attack.

    2. Venus Fly Trap: code\Assets\images\ennemies\flower.png

        - The Venus Fly Trap plant does not move; however, it attacks Crash Bandicoot if it gets too close by eating it. You can kill her by making a spin attack but not by jumping on her.

    3. Skunk: code\Assets\images\ennemies\skunk.png

        - The skunk has no attack, it just moves over a small area of the map. You can jump on it to kill it or by carrying out the spin attack.


4.  Others
    1. Character Models: code\Assets\images\images\personnages\crashspritesheet.png
    
        - Includes models for walking, jumping, attacking, etc. of characters.
    
    2. Background Image: code\Assets\images\images\imagesPlateforme\background.png
    
        - Background screen of the game.
    3. Dirt block: code\Assets\images\images\imagesPlateforme\DirtBlock.png
    
        - Game internal clay block material to achieve the border definition and the bottom foundation function.

    4. Grass Block: code\Assets\images\images\imagesPlateforme\grassDirtBlock.png
    
        - On top of the foundation, forming the basic ground and steps.
    5. Aku Aku Model:
    
        - 0 Level: code\Assets\images\images\imagesPlateforme\iconeAku0.png
        
            Aku Aku no longer has feathers and is transparent.
    
        - 1 Level: code\Assets\images\images\imagesPlateforme\iconeAku1.png
    
            Aku Aku has one feather that also acts as an icon for the Aku Aku level indication in the upper right corner of the game page.
    
        - 2 Level: code\Assets\images\images\imagesPlateforme\iconeAku2.png
        
            Aku Aku has two feather.
        
        - 3 Level: code\Assets\images\images\imagesPlateforme\iconeAku3.png
        
            Aku Aku has three feather.
    
    6. Character life indicator icon : code\Assets\images\images\imagesPlateforme\iconeCrash.png
    
        - The icon of the main character's life indication in the upper right corner of the game page.
    
    7. Wumpa fruit quantity indicator icon: code\Assets\images\images\imagesPlateforme\iconeWumpa.png
    
    8. Game main interface window icon : code\Assets\images\images\imagesPlateforme\logo.png
    
    9. Game start interface background image : code\Assets\images\images\imagesPlateforme\menu2.png


### Demake Logo

High Pixel Logo:

![00XR.png](https://s1.328888.xyz/2022/07/03/00XR.png)
![0uPB.png](https://s1.328888.xyz/2022/07/03/0uPB.png)

Low Pixel Logo:

![06uP.png](https://s1.328888.xyz/2022/07/03/06uP.png)

### Background
![0j3U.png](https://s1.328888.xyz/2022/07/03/0j3U.png)

---

## About

### About Team Sparrow

We are several students from University-365 & Hebei University of Technology in China. In a group project in 2021, member CHEN Yuqi first proposed the name and concept of Team Sparrow. Since then, Team Sparrow was officially established, and CHEN Yuqi also designed its logo and slogan—Small but Fully Functional.

To let you know, Team Sparrow are just a bunch of CS students who want to make something interesting by using their knowledge they know. We are not pro game studio or solution provider, but we have faith to provide you the best we can do.

Team Sparrow 2021 Member: CHEN Yuqi, CHENG Hanchang, KANG Weihao, YANG Chuhan, WANG Jinghao

Team Sparrow 2022 Member (for ): CHEN Yuqi, CHENG Hanchang, KANG Weihao, BU Deze, WANG Jinghao, ZHAO Chihao

Team Sparrow 2022 Member (for PHP Programming): CHEN Yuqi, CHENG Hanchang, KANG Weihao, WANG Jinghao

### About This Project 

Crash Bandicoot Demake - a Group Project of Hebut & University-365 Students

Last year, our AIR380 system ---- "Sparrow V1.0" received a lot of praise from social media.

And now, Team Sparrow presents you a retro game demake----Crash Bandicoot!

Why don't play our demake when you have nothing to do at home or quarantine?

The demo is free to play, with 3 complete maps. And the full version will launch after the insider review.

You can also view our project on GitHub, [Click Here](https://github.com/Lactorsj/Crash-Bandicoot-Demake).



### Crowdfunding

About crowdfunding, we launched our project at Ulule, you can see our project home page by [click here](https://www.ulule.com/01G6JK3YXPQ0KREJJ5HZFR23FD/).

However, due to the nationality limit of Ulule, we don't have any available invoice address, so we cannot submit the project to public. So we find another way to crowdfunding: A Campaign on social network.

We raise a hashtag: #TeamSparrowGame at April when we start developing this project. Since then, about 100 students from HEBUT and other university join our insider preview Kook(Chinese version of Discord) server.

They downloaded our source code from GitHub or directly from our server. We hear from them a lot and we make a lot of improvement thanks to our community.

This Campaign closed at July 3rd, 2022. We'll give some little gift to those who provided significent suggestions.

### Member Role and Division of Assignment

| Name  | Job |
| ---   | --- |
|CHEN Yuqi|Project manager|
|CHENG Hanchang|Developer|
|KANG Weihao|Designer|
|WANG Jinghao|Developer|
|BU Deze|Commercial|
|ZHAO Chihao|Designer|


* The project manager is the core of the team. CHEN Yuqi will arrange the division of labor for the project. When there is a problem in the project production, he will hold a meeting to discuss with the team members, analyze the problems of the project and give reasonable suggestions. Also, CHEN Yuqi will also do the drawing and commercial work.
* The developers of the project are the main implementers of the project code. When the project progress encounters difficulties, they will communicate with the project manager and designer to discuss more feasible solutions.
* The designer of the project is mainly responsible for the overall construction of the project, they are responsible for communicating with the client, and making specific designs for the client's ideas,
* The project manager is mainly responsible for the promotion of the product business, and they promote the project produced by the team. At the same time, pull investment for the project to attract more people to buy our products.

----
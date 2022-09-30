# cds-infrastructure
CDS Project Infrastructure - Where Projects Are Born, Hopefully

# Requirements
* Docker version 20.10.0 or later
* Git

# Before You Begin...
* Install Docker from the [official website](https://www.docker.com/).
* Install Git on [your computer](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

# My Project's Not Called cds-infrastructure! (Or, A Startup Guide for Any Enterprising Project Manager)
* Chill
* You'll be forking from this repo - and you can name the resulting repo [anything you want](https://github.blog/changelog/2022-04-12-you-can-now-name-your-fork-when-creating-it/)!
* On Github, fork this repo and rename it to reflect your incredible marketing skills (call it whatever you put on your project proposal, I guess).
* Now you've got a repo you can truly call your own, it's time to get to work getting set up!

# But I'm Working From Another Repo...
* That's perfectly fine!
* Let's say you're using an external repo
* You'll be importing that other repo as a [submodule](https://gist.github.com/gitaarik/8735255)!
* That way, you can build off of the external repo while accessing all of our wonderful utilities!
* First, **make sure to fork the other repo under [CDS' github organization](https://github.com/CornellDataScience).**
  * You don't want to be like [that one intern that accidentally made a change they weren't supposed to make](https://www.reddit.com/r/ProgrammerHumor/comments/og9ehq/intern_season_continues/), right?
* Next, clone your fork of cds-infrastructure (the one we made in the last section!) onto your computer using `git clone link_to_repo`
* Go into that folder.
* Run `git submodule add link_to_external_repo any_folder_name`
  * What this does is it adds the external repo you want to build off of (like something that a researcher made) as a submodule of your fork of cds-infrastructure!
  * Since it's under your fork, you are now free to do whatever you want to the repo while being able to access the nice things CDS' development infrastructure has to offer (like a nice Docker container to run your programs in so you don't end up trying to get environments to work for a month TT)
* Now that it's attached to your repo, commit the changes you've made in your project's main repo and push them to Github.
* Please check out the [Git Submodule Notes section](#submodules-for-dummies-or-how-to-work-with-submodules-and-avoid-panicking-at-3am) for some important information about working with nested repos. **Make sure you read it thoroughly so you avoid a lot of panicked 3AM Slack messages down the line!**

# But I'm Building My Own Repo...
* Great! That's wonderful! 
* In this case, you don't have to create a new submodule, but we *do* recommend building your repository from a new folder in the main project.
* The scripts are built with submodules in mind, so it's our recommendation that you keep as much of your project work in directories as possible (rather than leaving loose files in the root folder of your cds-infrastructure fork willy-nilly). 

# Submodules for Dummies (Or, How To Work With Submodules And Avoid Panicking At 3AM)
* You will need to run `git pull --recurse-submodules` instead of running a regular git pull
  * This will pull the latest code from the main repo as well as the latest updates to the submodule itself.
  * A regular git pull will not necessarily update the submodule code. 
* To update a project member's code to reflect your new submodule, they'll need to do the following:
  * First, run `git pull` to retrieve the submodule's information.
  * Next, run `git submodule init` to actually download all of the submodule's data.
  * **These steps are critical** - you want to make sure that everyone can access and update the submodule properly! Especially if you're working off of an existing repo - it gets **really easy** to lose a lot of time moving stuff around because you're not pushing updates where you think you're pushing them!
* Honestly, just read [the submodule documentation](https://gist.github.com/gitaarik/8735255). Then read it again. **Make sure you're following it to a T, and make sure your contributors are following it to a T.** It'll save you a lot of time and effort if you do!

# How to Build the Image
* Make sure Docker is running on your computer
* Go into your fork of cds-infrastructure
* Run `docker build .`
* Make sure it builds successfully. 
* Congratulations! You built a container! 🎊


//console.log("Playsong script is running")

/* Hide and show play pause button */

$(document).ready(function (){
    $("button#play_button").hide();
    $("button#play_button").click(function (){
        $("button#pause_button").show();
        $("button#play_button").hide();
    });
    $("button#pause_button").click(function (){
        $("button#play_button").show();
        $("button#pause_button").hide();
    });
    $("button#stop_button").click(function (){
        $("button#play_button").show();
        $("button#pause_button").hide();
    });
});

/* Player controls */

document.addEventListener("DOMContentLoaded", function() {
    startplayer();
    }, false);

    var player;
    let position;
    let seek;

    function startplayer()
    {
        player = document.getElementById('music_player');
        seekbar = document.getElementById("duration_slider");
        player.controls = false;
        player.volume=0.1
        player.play();
        
        /* Duration slider */
        
        player.addEventListener("timeupdate",(event) => {
            //console.log(event);
            let {currentTime, duration} = event.srcElement;
            //console.log(currentTime);
            //console.log(duration);
            let progress_time = (currentTime / duration) * 100;
            //console.log(progress_time);

            //console.log(player.currentTime,"live")

            //live time
            let min_progress = Math.floor(currentTime / 60);
            let sec_progress = Math.floor(currentTime % 60);
            let total_progress = `${min_progress}:${sec_progress}`;

            //total time or duration
            let min_duration = Math.floor(duration / 60);
            let sec_duration = Math.floor(duration % 60);
            let total_duration = `${min_duration}:${sec_duration}`;


            //console.log(Math.floor(progress_time),"aaaaaaaaaaaaaaaaa")
            document.getElementById("duration_slider").value=progress_time
            document.getElementById("start").innerHTML=total_progress
            document.getElementById("end").innerHTML=total_duration

            seekbar.addEventListener("click",(event) => {
                const { duration } = player
                let move_progress = (event.offsetX )
                //console.log(move_progress,"move_progress")
                player.currentTime = move_progress;
            });
        });

        player.addEventListener('ended',(event) => {
            document.getElementById("next").click();
        });
    }
    function play_aud()
    {
        player.play();
    } 
    function pause_aud()
    {
        player.pause();
    }
    function stop_aud()
    {
        player.pause();
        player.currentTime = 0;
    }
    function change_vol()
    {
        player.volume=document.getElementById("change_vol").value;
    }


    function notify()
    {
/*         ons.notification.alert("Successfully Added to Favourites"); */
        add_to_fav.action="/accounts/addtofavourite";
        add_to_fav.submit();
    }



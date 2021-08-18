<script src="https://unpkg.com/jquery/dist/jquery.min.js"></script>

$(document).ready(function (){
    $("ons-button#play_button").hide();
    $("ons-button#play_button").click(function (){
        $("ons-button#pause_button").show();
        $("ons-button#play_button").hide();
    });
    $("ons-button#pause_button").click(function (){
        $("ons-button#play_button").show();
        $("ons-button#pause_button").hide();
    });
    $("ons-button#stop_button").click(function (){
        $("ons-button#play_button").show();
        $("ons-button#pause_button").hide();
    });
});

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
    player.play();

    player.addEventListener("timeupdate",(event) => {
        //console.log(event);
        let {currentTime, duration} = event.srcElement;
        //console.log(currentTime);
        //console.log(duration);
        let progress_time = (currentTime / duration) * 100;
        //console.log(progress_time);

        console.log(player.currentTime,"live")

        //live time
        let min_progress = Math.floor(progress_time / 60);
        let sec_progress = Math.floor(progress_time % 60);
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
            console.log(move_progress,"move_progress")
            player.currentTime = move_progress;
        });
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
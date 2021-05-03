
// TOP BANNER
var rotor_messages = [

    '||| BANYAN VIDEOS |||',
    'PURVEYOURS OF FINE DVD & BLU-RAY VIDEOS',
    'FILMS RANGE FROM INDEPENDENT & BLOCKBUSTER!',
    'JOIN NOW FOR FREE!!!',
    'MEMBER ACCESS TO PREMIUM CONTENT!',
    'NEWS & FILM GOSSIP!',
    'FREQUENT SALES',
    'MEMBERS GET DISCOUNTS!',
    'JOIN NOW!!!',
    'ORDERS OVER £40.00, ITEMS SHIPPED FREE',

];

// ADVERT ROTOR
var rotor_count = 0;
function bannerRotor() {
    if (rotor_count < rotor_messages.length) {
        var insert = '<h1>' + rotor_messages[rotor_count] + '</h1>';
        $("#advert").html(insert);

        rotor_count++;
    }
    if (rotor_count == rotor_messages.length) {
        rotor_count = 0;
    }
    window.setTimeout("bannerRotor()", 5000);
}

// ARTICLE ROTOR
article_rotor_count = 0
article_rotor_max = 4

function articleRotor() {

    if (article_rotor_count < article_rotor_max) {

        var insert = "<h2>" + '{{ART.' + article_rotor_count + '.article_friendly_name}}' + "</h2>"

        $("#article_here").html(insert);

        article_rotor_count++;
    }
    if (article_rotor_count == article_rotor_max) {
        article_rotor_count = 0;
    }
    window.setTimeout("articleRotor()", 2000);
}



 



// function nRu() {

//     var element,name,arr;

//     element = document.getElementsByClassName('navbar-collapse');
//     // element.classList.remove('show');

//     name="show";
//     arr =element.className.split(" ");
//     if(arr.indexOf(name) ==-1 ){
//         element.className +=" " + name;
//     }


// }
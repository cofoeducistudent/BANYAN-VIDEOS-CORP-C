 
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
    'ORDERS OVER £30.00, ITEMS SHIPPED FREE',

];
var rotor_count = 0;

// CLASSIFIED HEADER
var c_ads = [

    'HAVE YOUR ADVERT PLACED HERE!',
    'CHEAP CLASSIFIED ADVERT SPACE',
    'CALL 078289 2787 9298',
   
];

var c_ads_count = 0;

// CLASSIFIEDS ROTOR
function rotate_c_ads() {
    if (c_ads_count < c_ads.length) {
        var insert = "<h1><em>" + c_ads[c_ads_count] + "<em></h1>";

        $( "#c_head" ).html(insert);
        c_ads_count ++;
    }

    if (c_ads_count == c_ads.length) {
        c_ads_count = 0;
    }
    window.setTimeout("rotate_c_ads()", 6000);
}








// ADVERT ROTOR
function bannerRotor() {
    if (rotor_count < rotor_messages.length) {
        var insert = '<h1>' + rotor_messages[rotor_count] + '</h1>';
        $( "#advert" ).html(insert);
       
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

        var insert ="<h2>"+ '{{ART.'+article_rotor_count+'.article_friendly_name}}' + "</h2>"
 
        $( "#article_here" ).html(insert);

        article_rotor_count++;
    }
    if (article_rotor_count == article_rotor_max) {
        article_rotor_count = 0;
    }
    window.setTimeout("articleRotor()", 2000);
}


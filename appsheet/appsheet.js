onReady = function() {
    $.getJSON('https://appsheettest1.azurewebsites.net/sample/posts', function(pics) {
        pictures = pics;

        //Error on invalid data result
        if (pics === null || pics.length === 0) {
            throw "Unable to fetch pictures";
        }
        $('#central').html('<h1>Lorem Story</h1>');
        
        for(var i = 0; i < pics.length; i++ ) {            
            var pic = pics[i];

            //validate pic obj
            if (pic.picture === undefined ||
                pic.text === undefined ||
                typeof(pic.picture) !== "string" ||
                pic.picture.split('/').length !== 5 ||
                typeof(pic.text) !== 'string') {
                throw "Invalic picture at index " + i;
            }
            
            var w = pic.picture.split('/')[3];
            var h = pic.picture.split('/')[4];

            //Give pictures random X offset to make it a bit more interesting
            var randxOffset = Math.random() * ($('#central').width()- 60 - parseInt(w)) + 30;
            
            var fonts = ['cursive', 'Impact', 'Georgia', 'Trebuchet MS', 'Courier New'];
            var font = fonts[Math.floor(Math.random() * fonts.length)];

            // Ideally would move this ugly long string into a template for readability
            // or use string interpolation, but figured since it's only a single line,
            // is acceptable for the scope of this project
            newPic = $('<div class="picbox" style="margin-left:' + randxOffset + 'px; width: ' +
                       (parseInt(w)) + 'px;"><img src="' + pic.picture + '" \><span><p>' +
                       firstCap(pic.text) + '</p></span></div>');

            newPic.find('p').attr('style', 'font-family:' + font + ';')
            $('#central').append(newPic);

            //Using textfill - a cool jquery plugin that automatically sizes text to size of container
            $(newPic).textfill({'maxFontPixels': 50, 'minFontPixels': 10, 'innerTag': 'p'});

            //saving element so it can be easily called from onClick
            pictures[i].obj = newPic;

            //Bind onClick event to new element
            $(newPic).on('click', i, onClick);
        }
    });

}

//Silly function to reload image on click
onClick = function(i) {
    i = i.data;
    pictures[i].obj.find('img').attr('src', pictures[i].picture + "?" + (new Date() - 1));
}

//Helper function for capializing first letter of pic text string
firstCap = function(str) {
    return str[0].toUpperCase() + str.slice(1);
}


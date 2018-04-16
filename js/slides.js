let featuredSlides = [];
let projectImgs = $(".featured-work img");
let mainImage = $(".main-image");
let mainText = $('.main-text');
let counter = 1;

for(let i of projectImgs) {
    featuredSlides.push(i.src);
}

window.setInterval(function() {
    counter = (counter + 1) % featuredSlides.length;
    let targetSlide = "url(" + featuredSlides[counter] + ")";
    mainImage.css("background-image", targetSlide)
}, 5000);

mainImage.change(function() {
    mainText.css('height', mainImage.css('height'));
});

mainImage.trigger('change');

let featuredSlides = [];
let projectImgs = $(".featured-work img");
let mainImage = $(".main-image");
let counter = 1;

for(let i of projectImgs) {
    featuredSlides.push(i.src);
}

window.setInterval(function() {
    let targetSlide = "url(" + featuredSlides[counter] + ")";
    mainImage.css("background-image", targetSlide)
    counter = (counter + 1) % featuredSlides.length;
}, 5000);

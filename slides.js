let featuredSlides = ["https://images.unsplash.com/photo-1452421822248-d4c2b47f0c81?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=b1a48d921059923e88ec28de5a615154&auto=format&fit=crop&w=1567&q=80"];
let projectImgs = $(".featured-work img");
let mainImage = $(".main-image");
let counter = 1;

for(let i of projectImgs) {
    featuredSlides.push(i.src);
}

window.setInterval(function() {
    let targetSlide = "url(" + featuredSlides[counter] + ")";
    mainImage.css("background-image", targetSlide)
    counter += 1;
    counter = counter % featuredSlides.length;
    console.log(targetSlide)
}, 5000);

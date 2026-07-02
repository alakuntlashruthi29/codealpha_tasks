let images = [
    "images/image1.jpg",
    "images/image2.jpg",
    "images/image3.jpg",
    "images/image4.jpg"
];

let currentIndex = 0;

function nextImage(){

    currentIndex++;

    if(currentIndex >= images.length){
        currentIndex = 0;
    }

    document.getElementById("gallery-image").src =
        images[currentIndex];
}

function prevImage(){

    currentIndex--;

    if(currentIndex < 0){
        currentIndex = images.length - 1;
    }

    document.getElementById("gallery-image").src =
        images[currentIndex];
}

function openLightbox(){

    document.getElementById("lightbox").style.display = "block";

    document.getElementById("lightbox-image").src =
        images[currentIndex];
}

function closeLightbox(){

    document.getElementById("lightbox").style.display = "none";
}
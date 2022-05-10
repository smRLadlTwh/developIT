$('.nav ul li').click(function () {

    $(this).addClass("active").siblings().removeClass('active');
})


const tabBtn = document.querySelectorAll('.nav ul li');
const tab = document.querySelectorAll('.tab');

function tabs(parse) {
    tab.forEach(function (node) {
        node.style.display = 'none';
    });
    if (parse == 2) {
        tab[parse].style.display='flex';
    }
    else {
        tab[parse].style.display='block';
    }
}
tabs(0);



let bio = document.querySelector('bio')
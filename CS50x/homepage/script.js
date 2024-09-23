document.addEventListener('DOMContentLoaded', function() {

    // Change Homepage to HOME when hover over
    let homepage = document.querySelector('#homepage');

    homepage.addEventListener('mouseenter', function() {
        homepage.innerHTML ='HOME';
    });

    homepage.addEventListener('mouseleave', function() {
        homepage.innerHTML ='Homepage';
    });

    // Secret
    let secret = document.querySelector('.secret');
    let clickhere = document.querySelector('.clickhere');
    clickhere.addEventListener('click', function() {
        clickhere.style.display = 'none';
        secret.style.display = 'block';
    });

});

let flag1 = false;
function showMoreItems(){
    const items = document.querySelector('#moreinc');
    if(!flag1){
        flag1=!flag1;
        items.style.display = 'block';
        document.getElementById('forJs').innerHTML = "ShowLess";
    }
    else{
        flag1=!flag1;
        items.style.display = 'none';
        document.getElementById('forJs').innerHTML = "More Process";
    }
} 
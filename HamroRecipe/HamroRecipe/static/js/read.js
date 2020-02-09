        let flag=false;
        function expand(){
            const val = document.querySelector('#content');
            if(!flag){
                flag = !flag;
                val.style.height = 'auto';
                document.getElementById("read").innerHTML="(-)";
            }else{
                flag = !flag;
                val.style.height = '0px';
                document.getElementById("read").innerHTML="readmore...";
            }
        }
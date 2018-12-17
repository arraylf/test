Vue.component('title1',{
    template:'<h1>猜数字游戏</h1>'
})
let vn=new Vue({
    el:'#app',
    data:{
        mes:'hello',
        rule:'谜底为4位0-9的不重复数字，玩家输入4位不重复数字,出数者就要根据这个数字给出几A几B，\
        其中A前面的数字表示位置正确的数的个数,而B前的数字表示数字正确而位置不对的数的个数,\
        当结果为4A0B时玩家获胜。',
        ans:'',
        input:'',
        output:'',
        sites:[],
    },
    mounted:function(){//生命周期函数运用，生成谜底。
        let a=[0,1,2,3,4,5,6,7,8,9];
        let b=[];
        let index;
        for (let i=0;i<4;i++){
            index=parseInt(Math.random()*(10-i));
            b.push(a[index]);
            a.splice(index,1);
        }
        this.ans=b;           
    },
    methods:{
        
        showRule(){
            alert(this.rule);
        },
        
        showAns(){
            alert(this.ans);
        },
        
        resume(){
            location.reload(); 
        },
       
        sub(){
            if (this.check()){
                let [l,A,B]=[[...this.input],0,0];
                for(let i=0;i<4;i++){
                    if (this.ans.includes(Number(l[i])) && l[i]!=this.ans[i])
                        {B+=1;}
                    if (l[i]==this.ans[i])
                        {A+=1;}
                }
                this.output=A+'a'+B+"b";
                let log={in:this.input,out:this.output};
                this.sites.push(log);
                this.input='';
            }
        },
        
        check(){
            let reg=/[0-9]{4}/;
            let arr=[...new Set(this.input)]
            if (!reg.test(this.input)){
                alert("error:请输入数字");
                return false;
            }
            if (this.input.length!=4){
                alert('error:请输入4位数字');
                return false;
            }
            if (arr.length!=4){
                alert('error:请输入非重复数字');
                return false;
            }
            return true;
        }

    },
    watch:{//监听输入，输入4位字符后自动提交。
        input:function(){
            if (this.input.length==4){
                this.sub();
            }
        },
            
    },
})

## gdbContextDiffer
Compare register context before/after executing the instruction.  
  
    가령, "lar" 이라는 인스트럭션이 있습니다.   
    구글에서 document 찾아봐도 설명도 부족하고.. 알아듣기도 힘들어요 ㅎㅅㅎ...  
    인스트럭션을 직접 실행 및 디버깅해보면 보다 쉽게 이해할 수 있습니다.  
    근데 디버깅하기 귀찮자나요 ㅎㅅㅎ...  
    그래서 인스트럭션 실행 전후로 레지스터 컨텍스트를 비교해주는 자동화 도구를 만들었습니다.  
<br>

## Prepare  
Set symbol *"here"* at the inspecting instruction.  
For example, if you're curious about *bsf*, set symbol like below.   
    
    [...omit...]   
    here:  
       bsf MYSYM, %ebx  
    [...omit...]  
    
<br>

## Run gdbdiff
    $ sudo apt-get install meld # graphical diff tools  
    $ git clone https://github.com/eternalklaus/gdbContextDiffer.git  
    $ cd gdbContextDiffer  
    $ python gdbdiff.py test.s  
<br>  

Enjoy gdbContextDiffer!  




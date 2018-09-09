2번. for.sh
/root/moduboan/(자신의 이름) 폴더 안에
*편의상 앞으로 위 경로를 '자기이름폴더' 라고 하겠습니다.
1, 2, 3, 4, 5 폴더를 만들어주세요.
(for문 or while문을 활용하여 만들어 주세요.)


#!/bin/bash

for i in {1..5}
do
	mkdir -p /root/moduboan/$i
done


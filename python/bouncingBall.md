한 아이가 큰 건물의 n층에서 공을 가지고 놀고 있다. 이 층의 높이는 알려져 있다.

`(float 형식의 매개변수 h는 미터 단위이며 h > 0)이다.`

아이가 공을 가지고 논다. 공은 2/3 정도의 높이로 튀어 오른다.

`(float 형식의 매개변수 "bounce"의 범위는 0 < bounce < 1)이다.`

아이의 어머니는 땅에서 1.5 미터 떨어진 창문을 내다 본다.

`(float 형식의 매개변수 "window"는 window < h 이다.`

어머니는 공이 창문 앞에서 **떨어지거나 튀는 것을** 몇 번이나 보게 되는가?

`위의 세 조건이 모두 충족되면 양의 정수를 반환하고 그렇지 않으면 -1을 반환합니다.`

**Note**

튀는 공의 높이가 window 매개 변수보다 엄격한 경우에만 볼을 볼 수 있음을 인정합니다.

**Example:**

> h = 3, bounce = 0.66, window = 1.5, result is 3
>
> h = 3, bounce = 1, window = 1.5, 결과는 -1 (Condition 2) 를 만족하지 않는다.).
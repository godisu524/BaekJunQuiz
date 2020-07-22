def solution(arrangement):
  answer = 0 # 잘린 쇠막대기의 총 개수
  arrangement = list(arrangement)
  bong = 0 # 쇠막대기 개수

  while arrangement:
    if arrangement[0] == "(": # 여는 괄호
      bong += 1
      arrangement.pop(0)
      if arrangement[0] == ")": # 괄호쌍 일 경우
        bong -= 1
        answer += bong
        arrangement.pop(0)
    else: # 닫는 괄호
      arrangement.pop(0)
      bong -= 1


      answer += 1

  return answer
# BPE (Byte Pair Encoding)

자주 등장하는 문자 쌍을 반복적으로 병합하여
서브워드(subword) 단위를 만드는 토크나이저 알고리즘이다.

초기에는 문자 단위 vocabulary로 시작하고,
가장 많이 등장하는 문자 쌍을 반복적으로 병합하면서
새로운 토큰을 생성하여 vocabulary를 확장한다.

이를 통해 OOV(Out Of Vocabulary) 문제를 줄이고
희귀 단어도 서브워드 조합으로 표현할 수 있다.

# NLG (Natural Language Generation)
자연어 처리는 크게 자연어 이해(NLU)와 자연어 생성(NLG)의 영역이 있다.
자연어 생성은 기계가 텍스트를 스스로 생성하는 영역을 말한다.
NLG 필요 분야 > image captioning, chatbot

# Neural Machine Translation
- 입력 문장(source text)을 번역한 출력 문장(target text)을 생성하는 Task
1950~1980 규칙기반 |RBMT|
1990~2015 통계기반 |SMT|
2015~ 신경망 기반 |NMT|

1. word embedding으로 인한 continuous representation의 힘
2. 기존 SMT가 여러 모듈이 결합된 결과였다면 이제는 end-to-end
3. attention으로 인해 길이가 긴 문장에서도 좋은 성능을 보이기 시작

# RNN Language Model
- RNN을 사용하면 언어모델 구현 가능
입력의 길이를 자유롭게 할 수 있으면서 임베딩층을 사용하여 워드 임베딩의 이점을 가진다.
이전 시점의 단어를 입력으로 받아 다음 단어를 예측하며, 문장의 마지막 시점까지 반복한다.

'cat'의 원-핫 벡터
실제값 : | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
cross entropy
예측값 : | 0.1 | 0.05 | 0.05 | 0.1 | 0.7 | 0.03 | 0.07 |

what (embedding) t = 1
will (embedding) t = 2
the (embedding)  t = 3
fat (embedding) t = 4

teacher forcing (교사 강요)
- RNN 언어 모델의 훈련 기법
- 테스트(추론) 단계에서는 현재 시점의 예측값이 다음 시점의 입력으로 사용된다.
- 훈련 단계에서 이것을 그대로 사용하면 학습이 불안정하거나 느려질 수 있다.
- 훈련 단계에서는 실제값(정답 토큰)을 다음 시점 입력으로 사용하여 빠르고 안정적으로 훈련한다.

RNN LM을 Bidirectional RNN으로 구현이 가능한가
> 다음 단어를 순차적으로 예측하는 전통적 언어모델 기준으로는 구조상 일반적으로 맞지 않는다.
(은닉층)

# Sequence-to-Sequence, seq2seq
- Sequence-to-Sequence는 입력된 시퀀스로부터 다른 도메인의 시퀀스를 출력한다.
ex) 챗봇, 기계 번역, 텍스트 요약 등
- seq2seq는 내부적으로 인코더와 디코더 구조를 가지고 있다.

논문참조 : RNN Encoder-Decoder for Statistical Machine Translation
- 인코더와 디코더 구조 제시 논문
- 통계 번역기에 이를 적용

논문참조 : Sequence to Sequence Learning with Neural Networks
- 본격적인 신경망 기계 번역기 제시
- 서로 다른 LSTM 아키텍처를 인코더-디코더로 사용

저는 ▶ 학생 ▶ 입니다 ▶ EOS ▶ I ▶ I ▶ am ▶ am ▶ a

- 인코더는 입력 문장의 모든 단어들을 순차적으로 입력받은 뒤 마지막에
이 모든 단어 정보들을 압축해서 context vector를 만든다.
- 디코더는 컨텍스트 벡터를 받아서 번역된 단어를 한 개씩 순차적으로 출력한다.
context vector : 인코더 정보들의 압축된 벡터

- 인코더의 마지막 은닉 상태를 컨텍스트 벡터라 부른다.
- 컨텍스트 벡터는 디코더 RNN 셀의 첫 번째 은닉 상태로 사용된다.
- 인코더와 디코더의 각 시점의 입력은 기본적으로 임베딩 벡터

LSTM (embedding, I) ▶ LSTM (embedding, am) ▶ LSTM (embedding, a) ▶ LSTM (embedding, student)
▶ context
▶ LSTM (embedding, <sos>) ▶ LSTM (embedding, je) ▶ LSTM (embedding, suis) ▶ LSTM (embedding, e'tudiant)
- 디코더는 RNN 언어모델이다. (teacher forcing 사용)
<sos> : 시작 심볼
<eos> : 종료 심볼
teacher forcing
- 기본적으로 훈련 단계에서 teacher forcing을 사용한다.
- 구현에 따라 teacher forcing 비율을 정해 수행할 수도 있으며, 이 비율은 파라미터가 될 수 있다.
- 이 비율을 높게 설정할수록 빠른 학습이 가능할 수 있으나, 학습 데이터에 과도하게 적응해 테스트 단계에서 악영향을 줄 수 있다.
- 테스트 단계에서는 teacher forcing을 사용할 수 없으므로 현 시점의 예측 출력을 다음 시점 입력으로 사용한다.

# Greedy Decoding
- seq2seq 디코더는 기본적으로 RNN 계열 모델로 설명되는 경우가 많다.
- 디코더는 매 시점마다 가장 높은 확률을 가지는 단어를 선택
- 매 순간 최적의 선택을 하지만, 전체적으로 봤을 때는 최적의 선택이 아닐 수 있음.
단점 : 잘못된 선택을 했더라도 그 결정을 취소할 수 없다.

ex.
인코더 입력
les pauvres sont de'munis (실제 정답 : the poor don't have any money)

decoder 생성
timestep 1 : the
step 2 : the poor
step 3 : the poor *are <- 뒤로 영향을 주는 잘못된 선택
step 4 : the poor are ??

※ greedy decoding 대신 beam search라는 알고리즘을 사용할 수 있다.
(몇 가지 가설을 세우고 최적의 선택지를 고른다.)

# Beam Search Decoding
- 매 시점마다 가장 확률 높은 k개의 다음 단어를 선택한 뒤 다음 시점 단어들의 확률을 예측
- k × vocab_size개의 후보군 중 다시 확률 높은 k개의 후보군만 선택, 나머지 단어 제거
- 매 시점마다 상위 k개의 후보군만 유지
- 항상 최적해를 보장하지 않지만 exhaustive search보다 효율적
- greedy search decoding이 놓칠 수 있는 더 나은 후보군을 유지할 수 있음

Beam Search Decoding (k = 3)
- 디코더의 매 스텝마다 정답 확률이 높은 k개의 선택지 추천(가설)
- 보통 5~10 크기 사용 (10 이상은 성능 개선 효과 거의 없음)

- 디코더 첫 번째 시점에 <start> 토큰이 입력됨 (sos, s, go 라고 하기도 함)
> start 토큰이 입력되면 디코더는 출력층에서 가장 확률 높은 k개의 단어를 고름
> 선택된 k개의 각각의 단어에 대해 다음 시점에서 또다시 가장 높은 확률의 k개 단어를 고름
> 다음 시점에서 또 가장 높은 확률의 k개 단어를 고름. 해당 시점 누적 확률 순으로 상위 k개 선택

<eos>를 만난 경우가 k개가 될 때까지 반복
<eos>가 선택되는 경우가 생기면 이는 최종 선택 후보

# Subword Tokenization
- 기계 번역 단어집합 크기는 30000~50000의 한정 크기를 가지지만
현실 단어 수는 훨씬 많음.
- 이로 인해 단어집합(vocab)에 없는 OOV(out-of-vocabulary) 문제 발생

논문 : Byte Pair Encoding
서브워드 단위 인코딩 제안

이후 >>
- Byte Pair Encoding의 여러 변형과
subword tokenizing 알고리즘들이 이어 제안됨.
- 기계 번역기에서 subword tokenizing 알고리즘은 이제 기본

- BPE 자체는 1994년 제안된 데이터 압축 알고리즘(NLP 아님!)
- 자주 등장하는 byte pair는 새로운 하나의 바이트가 됨
- 이를 단어 분리(word segmentation)에 도입 (NLP가 됨)
- bottom-up 방식 클러스터링
- 데이터의 모든 글자(char) 단위 유니그램 단어 사전에서 시작
- 자주 등장하는 바이그램을 유니그램으로 통합
- 모든 바이그램이 선택되거나 정해진 단어 집합 크기에 도달할 때까지 반복

dictionary
5 lo w
2 lo wer
6 n e w est
3 w i d est
> vocab
l,o,w,e,r,n,s,t,i,d,es,est,lo
>> iteration 3
l,o의 pair는 7의 빈도수를 가짐
l,o는 lo 병합


dictionary
5 low
2 low e r
6 n e w est
3 w i d est
> vocab
i,o,w,e,r,n,s,t,i,d,es,est,lo,low
>> iteration 4
lo,w의 pair는 7의 빈도수를 가짐
lo,w는 low 병합


dictionary
5 low
2 low e r
6 ne w est
3 w i d est
> vocab
i,o,w,e,r,n,s,t,i,d,es,est,lo,low,ne
>> iteration 5
n,e의 pair는 6의 빈도수를 가짐
n,e는 ne 병합

new est
>> iter 6 > 빈도 6, new 병합
newest
>> 7 new, est > newest
>> 8 wi, w,i 빈도 3, w,i > wi 병합
>>> 9 > wid 빈도 3
>>>> 10 > widest

(자주 등장하는 바이그램을 하나의 유니그램으로 병합)

- iteration할수록 집합의 크기는 커진다.
- 한국어(교착어) 적용 가능
- 자주 등장하는 바이그램은 그 자체가 단어로 취급
- 희귀 단어, OOV에 강건해짐

'low</w>': 5
low : char 단위 분할
</w> : 끝 의미
5 : 빈도수

'low</w>': 5, 'lower</w>': 2,
'n e w e s t</w>': 6, 'w i d e s t </w>': 3
> subword unit
>> es, est, est</w>, lo, low, ne, new, newest</w>, low</w>, wi
※ 단일 알파벳 별도 표기하지 않은 것임

# 한국어
sentence vs. mecab
- 채팅 데이터에 대해 실험
- 채팅 데이터는 띄어쓰기 오류, 오타, 신조어가 많아 OOV 자주 발생
- 실시간 채팅은 처리 속도에 매우 민감
- 단어 집합 크기를 30000, 50000, 100000으로 제한해 비교

mecab : 형태소 단위 잘 잡아냄
SentencePiece : mecab은 피스타치오(사전등록)는 잡아내나 SentencePiece는 전부 분리

<띄어쓰기 없는 문장도 참고>
origin. 엄청 빨리끝나는거같네
SentencePiece. 엄청 빨리끝나 는거같네
mecab. 엄청 빨리 끝나 는 거 같 네

origin. 후리스따뜻해?
SentencePiece. 후리스 따뜻해 ?
mecab. 후 리스 따뜻 해?

origin. 칭구들이랑 가죠 뭐
SentencePiece. 칭구들이랑 가죠 뭐
mecab. 칭 구 들 이랑 가 죠 뭐

# SentencePiece
- 아주 빠름
- subword 기반 토큰화로 unknown token(OOV) 문제를 완화할 수 있음
- 의미 단어가 잘 나눠지지 않을 수 있음

# Mecab
- SentencePiece만큼은 아니지만 충분히 빠름
- 형태소 기반, 의미 단어 잘 포착
- 신조어, 오타에 취약

# SentencePiece의 Detokenization
Detokenization : 서브워드 분리된 원문 복원
단어 시작에 _를 붙여 이를 참고해 기존 원문으로 자연스럽게 복원
주의 : 표시 안 해주면 복원 불가함.
'나는 오늘 아침밥을 먹었다.' > 토큰화 > ['_나는', '_오늘', '_아침', '밥', '을', '_먹', '었다', '.']
> 정수인코딩 > [4284, 552, 4269, 30456, 29636, 2570, 371, 29631]
> 역토큰화 > '나는 오늘 아침밥을 먹었다.'

# BLEU score
- 한 개의 문장에도 다양한 번역이 나올 수 있음
- 기계 번역 성능 측정을 위한 대표적인 방법 BLEU
- 논문 참고 : BLEU: a Method for Automatic Evaluation of Machine Translation
- 언어에 구애받지 않고 사용할 수 있으며, 계산이 빠름

BLEU = BP × exp(Σ w_n log p_n)

BP = { 1 if c > r, exp(1-r/c) if c ≤ r }

# unigram precision (유니그램 정밀도)
- 두 개의 기계 번역기가 존재한다고 하고 번역 문장을 candidate 1, 2 (번역기)
- 세 명의 사람에게 영작시킴. 만든 문장 reference 1, 2, 3 (실제 정답)
라고 가정

- ref 1, 2, 3 중 어느 한 문장에서라도 등장한 candidate 단어 개수 카운트 > 분자
- candidate 모든 단어 카운트 합 > 분모

unigram Precision = Ref들 중 존재하는 candidate 단어 수 / candidate 총 단어 수

ex.
Candidate : the the the the the the the

Ref1 : the cat is on the mat
Ref2 : there is a cat on the mat

말이 안 되는 번역인데 정밀도가 최고 성능? 중복 제거로 보정하기
새로운 카운트 방법 필요(Ref들과 Candidate를 고려한)

> Modified Unigram Precision
ex.
Candidate : the the the the the the the

Ref1 : the cat is on the mat
Ref2 : there is a cat on the mat

Modified Unigram Precision = 2/7

the : 중복 문제 해결되었으나
단순 count는 7이지만 max_ref_count는 2이므로
단어 the에 대한 최종 카운트인 Count_clip = min(7,2) = 2

ex.2
- candidate 1의 모든 단어 순서를 랜덤으로 뒤바꾼 candidate 3 추가
- candidate 1과 candidate 3의 unigram precision을 계산하면 두 값은 동일
- unigram precision은 단어 순서를 고려하지 않음

# N-gram precision (N = 2)
- unigram뿐 아니라 bigram, trigram처럼 연속된 n개 단어 묶음에 대해서도 precision을 계산할 수 있음.
N-gram precision
- BLEU는 보통 Modified 1-gram, 2-gram, 3-gram, 4-gram을 사용
- 이들을 각각 p1, p2, p3, p4라고 할 때 각각에 대한 가중치를 달리하여
합산한 뒤 BLEU를 계산

Pn : 각 gram의 보정된 정밀도
N : n-gram에서 n의 최대 숫자. 보통은 4의 값을 가짐. N이 4라는 것은 p1, p2, p3, p4 사용 의미.
Wn : 각 gram의 보정된 정밀도에 서로 다른 가중치를 줄 수 있음. 이 가중치의 합은 1로 함.
N을 4라고 하면, 동일한 가중치 0.25 모두 적용 가능

# 기계 번역기 과정
- 데이터 수집 : 병렬데이터 구매 or 크롤링
- 데이터 정제(cleaning) : 크롤링된 데이터에는 반드시 노이즈가 있음. (문장 단위 정렬, 특수문자 제거)
- 토크나이저 사용 : Mecab, SentencePiece 권장
- 데이터의 분리 : 학습 데이터, 검증 데이터, 테스트 데이터 분리
- 모델 선정 : seq2seq with Attention,
Transformer(아직 모르는 개념) 계열 모델 선정
- 학습 : 배치 크기, learning rate 같은 하이퍼파라미터 선정 후 GPU 통해 학습
- 추론(테스트) : Beam Search를 이용하여 테스트
- 역토큰화 : 번역된 문장을 역토큰화하여 자연스러운 문장 형태로 변환
- 성능평가 : BLEU, TER 등을 사용하여 모델 평가 후 개선
- 모델 배포 : 서버와 웹 서비스를 사용하여 실제 번역기를 서비스화

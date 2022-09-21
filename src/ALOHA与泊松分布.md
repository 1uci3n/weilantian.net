---
layout: post
title: ALOHA与泊松分布
slug: aloha
date: 2022-12-27 12:45
status: hidden
author: 魏蓝天
categories: 
  - MAC
tags: 
  - MAC
  - ALOHA
  - 分布
excerpt: ALOHA协议的吞吐量与泊松分布的理论推导
---

## ALOHA协议

- ALOHA协议的背景及用途：略
- ALOHA协议的基本流程：
  1. 当有需要发送的数据包时（此处称之为数据包可能不严谨，但是本文全用数据包来指代这个要发送的数据），直接发送。
  1. 接收端收到数据包时回复ACK，如果发送端没有接收到ACK经过随机的时间之后重发之前的数据包。

这种通信方式在多个用户与同一接收端进行通信时可能会引起混乱（碰撞，collision ）。
接下来通过排队论（queuing/queueing theory）分析ALOHA协议的效率。

## 排队论与泊松分布[^東京電機大学工学部情報通信工学科 坂本直志 2005年度情報ネットワーク教材]

假定随机生成的数据包有以下性质：
  1. 数据包的生成概率与时间无关（无记忆性）
  2. $1$单位时间平均有$\lambda$个数据包被发送

首先考虑一定时间内不产生数据包的概率，例如对于时刻$0,x,y,(0<x<y)$:

$p(0,x)$是$0$到$x$的时间段内不产生数据包的概率
$p(x,y)$是$x$到$y$的时间段内不产生数据包的概率
$p(0,y)$是$0$到$y$的时间段内不产生数据包的概率

此时我们有：
$$
p(0,x)\cdot p(x,y)=p(0,y)
$$
又由于无记忆性（概率只与时间段的长短相关，与时刻无关）：
$$
p(x,y)=p(0,y-x),\text{（时间段长度均为$y-x$）}
$$

接下来我们使用$P(T)$来表示$T$时间内不产生数据包的概率，那么$T+\Delta T$时间内不产生数据包的概率为：
$$
P(T+\Delta T)=P(T)\cdot P(\Delta T)
$$
所以对$P(T)$求导有：
$$
\frac{P(T+\Delta T)-P(T)}{\Delta T}=\frac{P(T)\cdot P(\Delta T)-P(T)}{\Delta T}=P(T)\frac{P(\Delta T)-1}{\Delta T}
$$

假设$\frac{P(\Delta T)-1}{\Delta T}$在$\Delta T\rightarrow0$时，收敛于$c_1$，那么上式两边取$\Delta T$的无穷小极限有：
$$
\frac{dP(T)}{dT}=c_1P(T)
$$

$$
\frac{dP(T)}{P(T)}=c_1dT
$$

$$
\int\frac{dP(T)}{P(T)}=\int c_1dT
$$

不定积分的常数用$c_2$表示， 有：
$$
\ln P(T)=c_1T+c_2
$$

$$
P(T)=\exp(c_1T+c_2)
$$

因为$P(0)=\exp(0+c_2)=0$，所以$c_2=0$，最终有：
$$
P(T)=\exp(c_1T)
$$
接下来我们考虑$T$时间内$k$个错误发生的概率$P_k(T)$该怎么表示。



- 当$k=1$时：

  考虑两种情况

  1. $T$时间内产生$1$个数据包，$\Delta T$时间内产生$0$个数据包
  2. $T$时间内产生$0$个数据包，$\Delta T$时间内产生$1$个数据包

  于是有：
  $$
  P_1(T+\Delta T)=P_1(T)P_0(\Delta T)+P_0(T)P_1(\Delta T)
  $$
  求导有：
  $$
  \frac{P_1(T+\Delta T)-P_1(T)}{\Delta T}=\frac{P_1(T)P_0(\Delta T)+P_0(T)P_1(\Delta T)-P_1(T)}{\Delta T}
  $$

  $$
  \frac{P_1(T+\Delta T)-P_1(T)}{\Delta T}=P_1(T)\frac{P_0(\Delta T)-1}{\Delta T}+\frac{P_0(T)P_1(\Delta T)}{\Delta T}
  $$

  这里$P_0(T)=P(T)$也就是上面推导的结果。此时再假设$\frac{P_1(\Delta T)}{\Delta T}$在$\Delta T\rightarrow0$时，收敛于$c_3$：
  $$
  \frac{dP_1(T)}{dT}=P_1(T)c_1+P_0(T)c_3
  $$

  $$
  \frac{dP_1(T)}{dT}=P_1(T)c_1+\exp(c_1T)c_3
  $$

  

  





[^東京電機大学工学部情報通信工学科 坂本直志 2005年度情報ネットワーク教材]:[東京電機大学工学部情報通信工学科 坂本直志 2005年度情報ネットワーク教材](http://edu.net.c.dendai.ac.jp/net/2005/9/index.xml)

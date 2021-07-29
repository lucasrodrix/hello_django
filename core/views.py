from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Olá {} de {} anos</h1>'.format(nome, idade))

def soma(request, v1, v2):
    return HttpResponse('O valor de soma de {} e {} é: {}'.format(v1, v2, v1+v2))

def subtracao(request, v1, v2):
    return HttpResponse('O valor de subtração de {} e {} é: {}'.format(v1, v2, v1-v2))

def multiplicacao(request, v1, v2):
    return HttpResponse('O valor de multiplicação de {} e {} é: {}'.format(v1, v2, v1*v2))

def divisao(request, v1, v2):
    return HttpResponse('O valor de divisão de {} e {} é: {}'.format(v1, v2, v1/v2))
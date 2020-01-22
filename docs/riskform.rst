Formulário de risco
===========

Relação de perguntas x respostas do formulário de risco para cada produto E&O, diferenciados por Pessoa Física e Pessoa Jurídica.

.. image:: images/terminology.png

Médicos - Pessoa Física
^^^^^^^^^^^^^^
Detalhamento do formulário de risco para o produto de Médicos Pessoa Física::

    [
      {
        "Id": 1,
        "Texto": "Você é novo segurado ou renovação de outra companhia?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Novo"
          },
          {
            "Id": 2,
            "Texto": "Renovação"
          }
        ]
      },
      {
        "Id": 2,
        "IdQuestaoPai": 1,
        "IdRespostaQuestaoPai": [
          "2"
        ],
        "Texto": "Nome da Companhia Anterior",
        "Obrigatório": "Não",
        "Tipo": "Texto Livre"
      },
      {
        "Id": 3,
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 2,
            "Texto": "Cirurgiões(Exceto Plástico), Anestesiologistas e Medicina Estética"
          },
          {
            "Id": 1,
            "Texto": "Sem Procedimentos Cirúrgicos"
          },
          {
            "Id": 3,
            "Texto": "Obstetras"
          }
        ]
      },
      {
        "Id": 4,
        "Texto": "Importância Segurada",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "R$ 30.000,00"
          },
          {
            "Id": 2,
            "Texto": "R$ 50.000,00"
          },
          {
            "Id": 3,
            "Texto": "R$ 75.000,00"
          },
          {
            "Id": 4,
            "Texto": "R$ 100.000,00"
          },
          {
            "Id": 5,
            "Texto": "R$ 150.000,00"
          },
          {
            "Id": 6,
            "Texto": "R$ 200.000,00"
          },
          {
            "Id": 7,
            "Texto": "R$ 250.000,00"
          },
          {
            "Id": 8,
            "Texto": "R$ 300.000,00"
          },
          {
            "Id": 9,
            "Texto": "R$ 400.000,00"
          },
          {
            "Id": 10,
            "Texto": "R$ 500.000,00"
          },
          {
            "Id": 11,
            "Texto": "R$ 600.000,00"
          },
          {
            "Id": 12,
            "Texto": "R$ 700.000,00"
          },
          {
            "Id": 13,
            "Texto": "R$ 800.000,00"
          },
          {
            "Id": 14,
            "Texto": "R$ 900.000,00"
          },
          {
            "Id": 15,
            "Texto": "R$ 1.000.000,00"
          }
        ]
      },
      {
        "Id": 5,
        "Texto": "CRM",
        "Obrigatório": "Sim",
        "Tipo": "Texto Livre"
      },
      {
        "Id": 6,
        "Texto": "Você já sofreu qualquer tipo de reclamação extrajudicial, processo judicial civil, criminal ou ético administrativo por dano(s) causado(s) pela prestação de seus serviços nos últimos 5 anos?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Nenhum"
          },
          {
            "Id": 2,
            "Texto": "1 sinistro"
          },
          {
            "Id": 3,
            "Texto": "2 sinistros"
          },
          {
            "Id": 4,
            "Texto": "3 sinistros ou mais"
          }
        ]
      },
      {
        "Id": 7,
        "IdQuestaoPai": 6,
        "IdRespostaQuestaoPai": [
          "2",
          "3",
          "4",
          "5",
          "6"
        ],
        "Texto": "Quantos sinistros nos últimos 12 meses?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Nenhum"
          },
          {
            "Id": 2,
            "Texto": "1 sinistro"
          },
          {
            "Id": 3,
            "Texto": "2 sinistros ou mais"
          }
        ]
      },
      {
        "Id": 8,
        "Texto": "Você tem conhecimento de qualquer fato ou circunstância que possa gerar uma reclamação extrajudicial, processo judicial civil, criminal ou ético administrativo ou de qualquer tipo similar de pedIdo de reparação de dano(s) causados(s) pela prestação de seus serviços?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Sim"
          },
          {
            "Id": 2,
            "Texto": "Não"
          }
        ]
      },
      {
        "Id": 9,
        "IdQuestaoPai": 8,
        "IdRespostaQuestaoPai": [
          "1"
        ],
        "Texto": "Nome dos Reclamantes",
        "Obrigatório": "Não",
        "Tipo": "Texto Livre"
      }
    ]

    

Médicos - Pessoa Jurídica
^^^^^^^^^^^^^^
Detalhamento do formulário de risco para o produto de Médicos Pessoa Jurídica::

    [
      {
        "Id": 1,
        "Texto": "Você é novo segurado ou renovação de outra companhia?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Novo"
          },
          {
            "Id": 2,
            "Texto": "Renovação"
          }
        ]
      },
      {
        "Id": 2,
        "IdQuestaoPai": 1,
        "IdRespostaQuestaoPai": [
          "2"
        ],
        "Texto": "Nome da Companhia Anterior",
        "Obrigatório": "Não",
        "Tipo": "Texto Livre"
      },
      {
        "Id": 3,
        "Texto": "Especialidade",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Home Care"
          },
          {
            "Id": 2,
            "Texto": "Clínica de Radiologia e Diagnóstico por Imagem"
          },
          {
            "Id": 3,
            "Texto": "Clínica de repouso, clínica psiquiátrica, clínica para tratamento dedependentes e riscos similares"
          },
          {
            "Id": 4,
            "Texto": "Transporte de pacientes"
          },
          {
            "Id": 5,
            "Texto": "Clínicas com cirurgia (exceto cirurgia plástica)"
          },
          {
            "Id": 6,
            "Texto": "Clínica sem cirurgia"
          },
          {
            "Id": 7,
            "Texto": "Clínicas de tratamento da dor e anestesiologia"
          },
          {
            "Id": 8,
            "Texto": "Laboratórios"
          },
          {
            "Id": 9,
            "Texto": "Clínicas de obstetrícia e reprodução humana"
          }
        ]
      },
      {
        "Id": 4,
        "Texto": "Importância Segurada",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "R$ 100.000,00"
          },
          {
            "Id": 2,
            "Texto": "R$ 150.000,00"
          },
          {
            "Id": 3,
            "Texto": "R$ 200.000,00"
          },
          {
            "Id": 4,
            "Texto": "R$ 250.000,00"
          },
          {
            "Id": 5,
            "Texto": "R$ 300.000,00"
          },
          {
            "Id": 6,
            "Texto": "R$ 500.000,00"
          }
        ]
      },
      {
        "Id": 5,
        "Texto": "Faturamento",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "R$ 50.000,00 - 100.000,00"
          },
          {
            "Id": 2,
            "Texto": "R$ 100.000,00 - 200.000,00"
          },
          {
            "Id": 3,
            "Texto": "R$ 200.000,00 - 300.000,00"
          },
          {
            "Id": 4,
            "Texto": "R$ 300.000,00 - 500.000,00"
          },
          {
            "Id": 5,
            "Texto": "R$ 500.000,00 - 1.000.000,00"
          },
          {
            "Id": 6,
            "Texto": "R$ 1.000.000,00 - 1.500.000,00"
          },
          {
            "Id": 7,
            "Texto": "R$ 1.500.000,00 - 2.000.000,00"
          },
          {
            "Id": 8,
            "Texto": "R$ 2.000.000,00 - 3.000.000,00"
          },
          {
            "Id": 9,
            "Texto": "R$ 3.000.000,00 - 5.000.000,00"
          },
          {
            "Id": 10,
            "Texto": "R$ 5.000.000,00 - 7.500.000,00"
          },
          {
            "Id": 11,
            "Texto": "R$ 7.500.000,00 - 10.000.000,00"
          }
        ]
      },
      {
        "Id": 6,
        "Texto": "Você já sofreu qualquer tipo de reclamação extrajudicial, processo judicial civil, criminal ou ético administrativo por dano(s) causado(s) pela prestação de seus serviços nos últimos 5 anos?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Nenhum"
          },
          {
            "Id": 2,
            "Texto": "1 sinistro"
          },
          {
            "Id": 3,
            "Texto": "2 sinistros"
          },
          {
            "Id": 4,
            "Texto": "3 sinistros ou mais"
          }
        ]
      },
      {
        "Id": 7,
        "IdQuestaoPai": 6,
        "IdRespostaQuestaoPai": [
          "2",
          "3",
          "4",
          "5",
          "6"
        ],
        "Texto": "Quantos sinistros nos últimos 12 meses?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Nenhum"
          },
          {
            "Id": 2,
            "Texto": "1 sinistro"
          },
          {
            "Id": 3,
            "Texto": "2 sinistros ou mais"
          }
        ]
      },
      {
        "Id": 8,
        "Texto": "Você tem conhecimento de qualquer fato ou circunstância que possa gerar uma reclamação extrajudicial, processo judicial civil, criminal ou ético administrativo ou de qualquer tipo similar de pedIdo de reparação de dano(s) causados(s) pela prestação de seus serviços?",
        "Obrigatório": "Sim",
        "Tipo": "Única escolha",
        "Respostas": [
          {
            "Id": 1,
            "Texto": "Sim"
          },
          {
            "Id": 2,
            "Texto": "Não"
          }
        ]
      },
      {
        "Id": 9,
        "IdQuestaoPai": 8,
        "IdRespostaQuestaoPai": [
          "1"
        ],
        "Texto": "Nome dos Reclamantes",
        "Obrigatório": "Não",
        "Tipo": "Texto Livre"
      }
    ]


Bikes
^^^^^^^^^^^^^^
Detalhamento do formulário de risco para o produto de Bikes::

    {
        "Identifier": "205a7953-1c7a-4dc3-8d7c-ef597807accf",
        "IdOperation": 14,
        "RiskAnalysis": [
            {
                //Você é novo segurado ou renovação de outra companhia?
                //Obrigatória
                //1 - Novo
                //2 - Renovação
                "questionId": 1,
                "answer": "1"
            },
            {
                //Qual a sua profissão?
                //Obrigatória
                //Texto livre
                "questionId": 2,
                "answer": "Desenvolvedor"
            },
            {
                //Modalidades
                //Obrigatório
                //Escolha 1 ou mais (Repita o bloco para respostas adicionais)
                //1 - Estrada
                //2 - Triatlo
                //3 - Mountain Bike
                //4 - Downhill
                "questionId": 3,
                "answer": "1"
            },
            {
                //Utilização
                //Obrigatório
                //Escolha 1 ou mais (Repita o bloco para respostas adicionais)
                //1 - Locomoção diária (trabalho, escola, etc)
                //2 - Lazer / Hobby
                //3 - Uso profissional
                "questionId": 4,
                "answer": "1"
            },
            {
                //Participa de Competições
                //Obrigatória
                //1 - Sim
                //2 - Não
                "questionId": 5,
                "answer": "1"
            },
            {
                //Treina em Assessoria Esportiva
                //Obrigatório
                //1 - Sim
                //2 - Não
                "questionId": 6,
                "answer": "1"
            },
            {
                //Locais onde Pedala
                //Obrigatório
                //Selecione 1 ou mais (Repita o bloco para respostas adicionais)
                //1 - Área Urbana
                //2 - Auto Estrada
                //3 - Campo ou Estradas de Terra
                //4 - Montanha
                "questionId": 7,
                "answer": "1"
            },
            {
                //Frequência de Treino
                //Obrigatório (Escolha 1)
                //1 - 1 a 2 vezes / semana
                //2 - 3 a 5 vezes / semana
                //3 - mais de 5 vezes
                "questionId": 8,
                "answer": "1"
            },
            {
                //Descrição da Bicicleta
                //Obrigatório
                //Texto Livre
                "questionId": 9,
                "answer": "Texto Livre"
            },
            {
                //Local de Compra
                //Obrigatório
                //Texto Livre
                "questionId": 10,
                "answer": "Texto Livre"
            },
            {
                //Valor de Mercado
                //Obrigatório
                //Valor Decimal
                "questionId": 11,
                "answer": "3000"
            },
            {
                //Número de Série
                //Obrigatório
                //Texto Livre
                "questionId": 12,
                "answer": "Texto Livre"
            },
            {
                //Bike Nova (0km)
                //Obrigatório (Escolha uma opção)
                //1 - Sim
                //2 - Não
                "questionId": 13,
                "answer": "1"
            },
            {
                //Ano de Fabricação
                //Obrigatório
                //Número
                "questionId": 14,
                "answer": "2016"
            },
            {
                //Possui Nota Fiscal?
                //Obrigatório (Escolha uma opção)
                //1 - Sim
                //2 - Não
                "questionId": 15,
                "answer": "Texto Livre"
            },
            {
                //Bike Original
                //Obrigatório (Escolha uma opção)
                //1 - Sim
                //2 - Não
                "questionId": 16,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Quadro
                //Opcional
                //Texto Livre
                "questionId": 17,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Pedivela
                //Opcional
                //Texto Livre
                "questionId": 18,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Câmbio Traseiro
                //Opcional
                //Texto Livre
                "questionId": 19,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Selim
                //Opcional
                //Texto Livre
                "questionId": 20,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Mesa
                //Opcional
                //Texto Livre
                "questionId": 21,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Trocador Traseiro
                //Opcional
                //Texto Livre
                "questionId": 22,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Cubos
                //Opcional
                //Texto Livre
                "questionId": 23,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Pneus
                //Opcional
                //Texto Livre
                "questionId": 24,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Cor
                //Opcional
                //Texto Livre
                "questionId": 25,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Tamanho
                //Opcional
                //Texto Livre
                "questionId": 26,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Garfo
                //Opcional
                //Texto Livre
                "questionId": 27,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Freios
                //Opcional
                //Texto Livre
                "questionId": 28,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Câmbio Dianteiro
                //Opcional
                //Texto Livre
                "questionId": 29,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Canote
                //Opcional
                //Texto Livre
                "questionId": 30,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Guidão
                //Opcional
                //Texto Livre
                "questionId": 31,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Trocador Dianteiro
                //Opcional
                //Texto Livre
                "questionId": 32,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Rodas
                //Opcional
                //Texto Livre
                "questionId": 33,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Pedal
                //Opcional
                //Texto Livre
                "questionId": 34,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Número de Marchas
                //Opcional
                //Texto Livre
                "questionId": 35,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Clip
                //Opcional
                //Texto Livre
                "questionId": 36,
                "answer": "Texto Livre"
            }
        ],
        //Dados do Proponente (Todos os campos abaixo são obrigatórios)
        "PersonalData": {
            "Name": "Test User",
            "Email": "email@argo.com",
            "Identity": "00000000000"
        },
        //Fotos da Bike e/ou Nota Fiscal.
        "Documents": [
            {
                "Name": "teste.jpg",
                "File": "" // enviar o base64 do arquivo
            },
            {
                "Name": "teste1.jpg",
                "File": "" // enviar o base64 do arquivo
            },
            {
                "Name": "teste2.jpg",
                "File": "" // enviar o base64 do arquivo
            },
            {
                "Name": "teste3.jpg",
                "File": "" // enviar o base64 do arquivo
            }
        ]
    }
Contributing
============

Contributions to this repository are welcome and encouraged.

All members of our community are expected to follow Read the Docs' `Code of Conduct`_. Please make sure you are welcoming and friendly in all of our spaces.

.. _Code of Conduct: https://docs.readthedocs.io/en/latest/code-of-conduct.html

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




Adding new themes
-----------------

Adding a new theme to this repository is relatively straight-forward. The steps include:

- Adding the branch name to the theme mapping to `conf.py` (see `branch_to_theme_mapping`). The name of the branch should closely follow the theme name.
- Updating the `README.rst` to link to the docs on Read the Docs
- Create an issue that a maintainer needs to create a new branch on the repository and configure Read the Docs to build docs on the new branch.

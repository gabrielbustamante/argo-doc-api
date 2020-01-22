Cotação
==================


Obter cotação
^^^^^^^^^^^^^^
Serviço utilizado para se recuperar ou obter os dados de uma cotação utilizando o identificador único no retorno da cortação.

**Endpoint**

::

    GET {{URL_AMBIENTE}}/quotation/api/quotation?identifier=c051cb56-6b95-4741-9bc2-6caf9978252d


**Response**

::

     asdsadasda




Realizar cotação.
^^^^^^^^^^^^^^
Serviço utilizado para soliciatar cotação.


``IdOperation``
    Identificador da operação utilizada.
``EffectiveDate``
   Data de inicio da contratação (Formato: AAAA/MM/DD)
``RiskAnalysis`` 
    Seção referente as perguntas e respostas do respectivo formulário de risco

    ``questionId`` Id da questão

    ``answer`` Resposta da questão
    
``PersonalData`` 
    Seção referente as informações do segurado da apólice (Devem ser as mesmas informadas no momento de realizar uma cotação).

    ``Name`` Nome

    ``Email`` E-mail

    ``Identity`` CPF/CNPJ do segurado


**Endpoint**

::

    POST {{URL_AMBIENTE}}/quotation/api/quotation/


**Exemplo Médicos PF**

::

    {
        "IdOperation": "35",
        "RiskAnalysis": [
            {
                "questionId": "1",
                "answer": "1"
            },
            {
                "questionId": "2",
                "answer": "2"
            },
            {
                "questionId": "3",
                "answer": "1"
            },
            {
                "questionId": "4",
                "answer": "3"
            },
            {
                "questionId": "5",
                "answer": "3213213213"
            },
            {
                "questionId": "6",
                "answer": "1"
            },
            {
                "questionId": "7",
                "answer": "1"
            },
            {
                "questionId": "8",
                "answer": "2"
            },
            {
                "questionId": "9",
                "answer": ""
            }
        ],
        "PersonalData": {
            "Name": "Gabriel Bustamante",
            "Email": "argo@argo.com",
            "Identity": "05382323070"
        },
        "EffectiveDate": "2019-05-20"
    }

**Exemplo Bikes**

::

    {
        "Identifier": "205a7953-1c7a-4dc3-8d7c-ef597807accf",
        "IdOperation": 14,
        "RiskAnalysis": [
            {
                "questionId": 1,
                "answer": "1"
            },
            {
                "questionId": 2,
                "answer": "Desenvolvedor"
            },
            {
                "questionId": 3,
                "answer": "1"
            },
            {
                "questionId": 4,
                "answer": "1"
            },
            {
                "questionId": 5,
                "answer": "1"
            },
            {
                "questionId": 6,
                "answer": "1"
            },
            {
                "questionId": 7,
                "answer": "1"
            },
            {
                "questionId": 8,
                "answer": "1"
            },
            {
                "questionId": 9,
                "answer": "Texto Livre"
            },
            {
                "questionId": 10,
                "answer": "Texto Livre"
            },
            {
                "questionId": 11,
                "answer": "3000"
            },
            {
                "questionId": 12,
                "answer": "Texto Livre"
            },
            {
                "questionId": 13,
                "answer": "1"
            },
            {              
                "questionId": 14,
                "answer": "2016"
            },
            {
                "questionId": 15,
                "answer": "Texto Livre"
            },
            {
                "questionId": 16,
                "answer": "Texto Livre"
            },
            {
                "questionId": 17,
                "answer": "Texto Livre"
            },
            {
                "questionId": 18,
                "answer": "Texto Livre"
            },
            {
                "questionId": 19,
                "answer": "Texto Livre"
            },
            {
                "questionId": 20,
                "answer": "Texto Livre"
            },
            {
                "questionId": 21,
                "answer": "Texto Livre"
            },
            {
                "questionId": 22,
                "answer": "Texto Livre"
            },
            {
                "questionId": 23,
                "answer": "Texto Livre"
            },
            {
                "questionId": 24,
                "answer": "Texto Livre"
            },
            {
                "answer": "Texto Livre"
            },
            {
                "answer": "Texto Livre"
            },
            {
                "questionId": 27,
                "answer": "Texto Livre"
            },
            {
                //Modificações - Freios
                "questionId": 28,
                "answer": "Texto Livre"
            },
            {
                "questionId": 29,
                "answer": "Texto Livre"
            },
            {
                "questionId": 30,
                "answer": "Texto Livre"
            },
            {
                "questionId": 31,
                "answer": "Texto Livre"
            },
            {
                "questionId": 32,
                "answer": "Texto Livre"
            },
            {
                "questionId": 33,
                "answer": "Texto Livre"
            },
            {
                "questionId": 34,
                "answer": "Texto Livre"
            },
            {
                "questionId": 35,
                "answer": "Texto Livre"
            },
            {
                "questionId": 36,
                "answer": "Texto Livre"
            }
        ],
        "PersonalData": {
            "Name": "Test User",
            "Email": "email@argo.com",
            "Identity": "00000000000"
        },
        "Documents": [
            {
                "Name": "bike.jpg",
                "File": ""
            },
            {
                "Name": "bike1.jpg",
                "File": ""
            },
            {
                "Name": "bike2.jpg",
                "File": ""
            },
            {
                "Name": "bike3.jpg",
                "File": ""
            }
        ]
    }

.. Note:: You can use the `IdentityModel <https://github.com/IdentityModel/IdentityModel2>`_ client library to programmatically create authorize requests .NET code. For more information check the IdentityModel `docs <https://identitymodel.readthedocs.io/en/latest/client/authorize.html>`_.

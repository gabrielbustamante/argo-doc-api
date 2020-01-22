Cotação
==================

Requisição para realizar uma nova cotação.

.. Note:: .

``IdOperation``
    Identificador da operação utilizada.
``EffectiveDate``
   Data de inicio da contratação (Formato: AAAA/MM/DD)
``RiskAnalysis`` 
    Seção referente as perguntas e respostas do formulário de risco
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


**Body**

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


.. Note:: You can use the `IdentityModel <https://github.com/IdentityModel/IdentityModel2>`_ client library to programmatically create authorize requests .NET code. For more information check the IdentityModel `docs <https://identitymodel.readthedocs.io/en/latest/client/authorize.html>`_.

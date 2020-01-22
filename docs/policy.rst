Apólices
===========

.. image:: images/terminology.png

Obter parcelas
^^^^^^^^^^^^^^
Serviço para obter o status de pagamento das parcelas e no caso do boleto o pdf do documento.

**Endpoint**

::

    GET {{URL_AMBIENTE}}/policy/api/installments?certificateNumber={Número do Certificado}


**Response**

::

     asdsadasda



Obter Certificado
^^^^^^^^^^^^^^
Serviço utilizado para se obter o certificado em PDF. Dados de entrada: CPF/CNPJ do segurado, Número do Certificado, CNPJ do corretor.

**Endpoint**

::

    GET {{URL_AMBIENTE}}/policy/api/policies/detail/{Número do Certificado}


**Response**

::

     asdsadasda



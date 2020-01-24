Apólices
===========

Obter parcelas
^^^^^^^^^^^^^^
Serviço para obter o status de pagamento das parcelas.

``certificateNumber`` Número do certificado, gerado após o Checkout.

**Endpoint**

::

    GET {{URL_AMBIENTE}}/policy/api/installments?certificateNumber={Número do Certificado}


.. code-block:: json

    {
      "application/json": {
          "installments": [
              {
                  "installmentNumber": 1,
                  "paid": true,
                  "value": 150.00,
                  "valuePaid": 150.00,
                  "billingDate": "2019-11-23T00:00:00"
              },
              {
                  "installmentNumber": 2,
                  "paid": true,
                  "value": 150.00,
                  "valuePaid": 150.00,
                  "billingDate": "2019-12-23T00:00:00"
              },
              {
                  "installmentNumber": 3,
                  "paid": true,
                  "value": 160.00,
                  "valuePaid": 160.00,
                  "billingDate": "2020-01-23T00:00:00"
              }
          ]
      }
    }


"""
        Here is another function.

        :param a: The number of green hats you own.
        :type a: int

        :param b: The number of non-green hats you own.
        :type b: int

        :param kwargs: Additional keyword arguments. Each keyword parameter
                       should specify the name of your favorite cuisine.
                       The values should be floats, specifying the mean price
                       of your favorite dish in that cooking style.
        :type kwargs: float

        :returns: A 2-tuple.  The first element is the mean price of all dishes
                  across cuisines.  The second element is the total number of
                  hats you own: :math:`a + b`.
        :rtype: tuple


Obter Certificado
^^^^^^^^^^^^^^
Serviço utilizado para se obter o certificado em PDF.

``certificateNumber`` Número do certificado, gerado após o Checkout.

**Endpoint**

::

    GET {{URL_AMBIENTE}}/policy/api/policies?certificateNumber={Número do Certificado}


**Response**

::

    {
        "documents": [
            {
                "hasGenerated": true,
                "id": 96940,
                "name": "E&O Templates",
                "url": "https://azuq2brapi.blob.core.windows.net/documents/1f8ca969-eb64-48b1-8e99-991c8684d929/0035202000000000057"
            }
        ]
    }



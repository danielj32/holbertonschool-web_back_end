import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, currency) {
      if (typeof amount !== 'number' || !(currency instanceof Currency)) {
        throw (TypeError('wrong parameter type'));
      }
      this.__amount = amount;
      this.__currency = currency;
    }

    get amount() {
      return this.__amount;
    }

    get currency() {
      return this.__currency;
    }

    set amount(amount) {
      if (typeof amount !== 'number') {
        throw (TypeError('wrong parameter type'));
      }
      this.__amount = amount;
    }

    set currency(currency) {
      if (!(currency instanceof Currency)) {
        throw (TypeError('wrong parameter type'));
      }
      this.__currency = currency;
    }

    displayFullPrice() {
      return `${this.__amount} ${this.__currency.name} (${this.__currency.code})`;
    }

    static convertPrice(amount, conversionRate) {
      return amount * conversionRate;
    }
  }

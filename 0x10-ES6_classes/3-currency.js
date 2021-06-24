export default class Currency {
    constructor(code, name) {
      if (typeof code === 'string' && typeof name === 'string') {
        this.__code = code;
        this.__name = name;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    get name() {
      return this.__name;
    }
  
    get code() {
      return this.__code;
    }
  
    set name(name) {
      if (typeof name === 'string') {
        this.__name = name;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    set code(code) {
      if (typeof code === 'string') {
        this.__code = code;
      } else {
        throw (TypeError('Attributes must be strings'));
      }
    }
  
    displayFullCurrency() {
      return `${this.__name} (${this.__code})`;
    }
  }

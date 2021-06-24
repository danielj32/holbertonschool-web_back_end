export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !(this.evacuationWarningMessage)) {
      throw (Error('Class extending Building must override evacuationWarningMessage'));
    }
    if (typeof sqft !== 'number') {
      throw (TypeError('sqft must be an integer'));
    }
    this.__sqft = sqft;
  }

  get sqft() {
    return this.__sqft;
  }
}

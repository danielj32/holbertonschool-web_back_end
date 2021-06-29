export default function createInt8TypedArray(length, position, value) {
  try {
    const buff = new ArrayBuffer(length);
    const views = new DataView(buff);
    views.setInt8(position, value);
    return views;
  } catch (i) {
    throw Error('Position outside range');
  }
}

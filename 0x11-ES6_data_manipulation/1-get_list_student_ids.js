export default function getListStudentIds(bjs) {
  if (Array.isArray(bjs) === false) {
    return [];
  }
  return bjs.map((y) => y.id);
}

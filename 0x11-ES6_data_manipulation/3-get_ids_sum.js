export default function getStudentIdsSum(students) {
  if (Array.isArray(students) === false) {
    return 0;
  }
  let get_sum = (sum, i) => sum + i.id;
  return students.reduce(get_sum, 0);
}

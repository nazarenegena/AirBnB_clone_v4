$(document).ready(function () {
  let selectedAmenities = {};
  $(document).on('change', "input[type='checkbox']", function () {
    if (this.checked) {
      selectedAmenities[$(this).data('id')] = $(this).data('name');
    } else {
      delete selectedAmenities[$(this).data('id')];
    }
    let amenities = Object.values(selectedAmenities);
    if (amenities.length > 0) {
      $('div.amenities > h4').text(Object.values(checkedAmenities).join(', '));
    } else {
      $('div.amenities > h4').html('&nbsp;');
    }
  });
});

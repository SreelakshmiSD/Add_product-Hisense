// COUNTRY
$(document).ready(function() {

    $("#CountryForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#CountryForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#country-submit").attr("disabled", "disabled");
                    $("#country-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    console.log(response.message)

                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            alert('form')                    
                            $('#country-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#country-submit").attr("disabled", false);
                    $("#country-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_country', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/country/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#country-form-div').html('Loading...')
        },
        success: function(response) { 
            // console.log(response.template)
            $('#country-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})

function FilterCountry(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_country').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#country-tbody').html(response.template)
            $('#country-pagination').html(response.pagination)
        },
    });
}

function DeleteCountry(id) {
    console.log(id)
    var url = '/country/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterCountry('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}





$(document).on('click', '.country-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('country-edit').getAttribute('data-country-id');
    var id = $(this).data('country-id');

    var url = '/country/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#country-form-div').html('Loading...')
        },
        success: function(response) {
            $('#country-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})


// Region

$(document).ready(function() {

    $("#RegionForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#RegionForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#region-submit").attr("disabled", "disabled");
                    $("#region-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    console.log(response.message)

                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            alert('form')                    
                            $('#region-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#region-submit").attr("disabled", false);
                    $("#region-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_region', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/region/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#region-form-div').html('Loading...')
        },
        success: function(response) { 
            console.log(response)
            // console.log(response.template)
            $('#region-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})


$(document).on('click', '.region-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('region-edit').getAttribute('data-region-id');
    var id = $(this).data('region-id');

    console.log(id)
    var url = '/region/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#region-form-div').html('Loading...')
        },
        success: function(response) {
            console.log(response)
            $('#region-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})


function FilterRegions(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_region').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#region-tbody').html(response.template)
            $('#region-pagination').html(response.pagination)
        },
    });
}

function DeleteRegion(id) {
    console.log(id)
    var url = '/region/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterRegions('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}




// BRAND

$(document).on('click', '#create_brand', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/brand/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#brand-form-div').html('Loading...')
        },
        success: function(response) { 
            console.log(response)
            // console.log(response.template)
            $('#brand-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})

$(document).ready(function() {

    $("#BrandForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#BrandForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#brand-submit").attr("disabled", "disabled");
                    $("#brand-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                              
                        } else {     
                            alert('form')                    
                            $('#brand-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#brand-submit").attr("disabled", false);
                    $("#brand-submit").val("Save");
                },
            });
        },
    });
});

function FilterBrand(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_brand').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#brand-tbody').html(response.template)
            $('#brand-pagination').html(response.pagination)
        },
    });
}


function DeleteBrand(id) {
    console.log(id)
    var url = '/brand/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterBrand('')
                        location.reload(true);

                        
                
                    }
                },
            });
        }
    });
}

$(document).on('click', '.brand-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('brand-edit').getAttribute('data-brand-id');
    var id = $(this).data('brand-id');

    var url = '/brand/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#brand-form-div').html('Loading...')
        },
        success: function(response) {
            console.log(response)
            $('#brand-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})



// DIVISION
$(document).ready(function() {

    $("#DivisionForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {
            event.preventDefault();
            var formData = $("#DivisionForm").serializeArray();
            // console.log(formData)
            formData.forEach(function(field) {
                if (field.name === "brand") {
                  field.value = parseInt(field.value);
                }
              });
            console.log(formData)
            
            var url = $("#form_url").val()
            

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#division-submit").attr("disabled", "disabled");
                    $("#division-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    // console.log(response.message)

                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            // alert('form')  
                            // console.log(response.template)                  
                            $('#division-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#division-submit").attr("disabled", false);
                    $("#division-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_division', function(event) {

    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/division/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#division-form-div').html('Loading...')
        },
        success: function(response) { 
            // console.log(response)
            $('#division-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})

$(document).on('click', '.division-edit', function(event) {
    event.preventDefault();
    // var id = document.getElementById('division-edit').getAttribute('data-division-id');
    var id = $(this).data('division-id');
    console.log(typeof id)
    var url = '/division/' + id + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#division-form-div').html('Loading...')
        },
        success: function(response) {
            $('#division-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})


function FilterDivision(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_division').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#division-tbody').html(response.template)
            $('#division-pagination').html(response.pagination)
        },
    });
}




function DeleteDivision(id) {
    console.log(id)
    var url = '/division/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterDivision('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}







// CATEGORY

$(document).ready(function() {

    $("#CategoryForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#CategoryForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#category-submit").attr("disabled", "disabled");
                    $("#category-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    console.log(response.message)

                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            alert('form')                    
                            $('#category-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#category-submit").attr("disabled", false);
                    $("#category-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_category', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/category/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#category-form-div').html('Loading...')
        },
        success: function(response) { 
            console.log(response)
            // console.log(response.template)
            $('#category-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})

$(document).on('click', '.category-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('category-edit').getAttribute('data-category-id');
    var id = $(this).data('category-id');

    var url = '/category/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#category-form-div').html('Loading...')
        },
        success: function(response) {
            console.log(response)
            $('#category-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})

function FilterCategory(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_category').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#category-tbody').html(response.template)
            $('#category-pagination').html(response.pagination)
        },
    });
}

function DeleteCategory(id) {
    console.log(id)
    var url = '/category/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterCountry('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}



// SUBCATEGORY

$(document).ready(function() {

    $("#SubcategoryForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#SubcategoryForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#subcategory-submit").attr("disabled", "disabled");
                    $("#subcategory-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    console.log(response.message)

                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            alert('form')                    
                            $('#subcategory-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#subcategory-submit").attr("disabled", false);
                    $("#subcategory-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_subcategory', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/subcategory/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#subcategory-form-div').html('Loading...')
        },
        success: function(response) { 
            console.log(response)
            // console.log(response.template)
            $('#subcategory-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})


$(document).on('click', '.subcategory-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('subcategory-edit').getAttribute('data-subcategory-id');
    var id = $(this).data('subcategory-id');
    
    var url = '/subcategory/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#subcategory-form-div').html('Loading...')
        },
        success: function(response) {
            console.log(response)
            $('#subcategory-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})


function FilterSubcategory(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_subcategory').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#subcategory-tbody').html(response.template)
            $('#subcategory-pagination').html(response.pagination)
        },
    });
}

function DeleteSubcategory(id) {
    console.log(id)
    var url = '/subcategory/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterCountry('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}



// SKU CLASSIFICATION
$(document).ready(function() {

    $("#Sku_classificationForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#Sku_classificationForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#skuclassification-submit").attr("disabled", "disabled");
                    $("#skuclassification-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    console.log(response.message)

                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            alert('form')                    
                            $('#sku_classification-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#skuclassification-submit").attr("disabled", false);
                    $("#skuclassification-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_skuclassification', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/sku_classification/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#skuclassification-form-div').html('Loading...')
        },
        success: function(response) { 
            console.log(response)
            // console.log(response.template)
            $('#skuclassification-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})

$(document).on('click', '.skuclassification-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('skuclassification-edit').getAttribute('data-skuclassification-id');
    var id = $(this).data('skuclassification-id');
    
    var url = '/sku_classification/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#skuclassification-form-div').html('Loading...')
        },
        success: function(response) {
            console.log(response)
            $('#skuclassification-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})


function FilterSkuClassification(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_skuclassification').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#skuclassification-tbody').html(response.template)
            $('#skuclassification-pagination').html(response.pagination)
        },
    });
}


function Delete_sku_classification(id) {
    console.log(id)
    var url = '/sku_classification/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterCountry('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}


// SCREENSIZE

$(document).ready(function() {

    $("#ScreensizeForm").validate({

        rules: {},
        messages: {},

        submitHandler: function(form, event) {

            event.preventDefault();
            var formData = $("#ScreensizeForm").serializeArray();
            var url = $("#form_url").val()
            console.log(formData)

            $.ajax({
                url: url,
                headers: {
                    "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
                },
                method: "POST",
                data: formData,
                beforeSend: function() {
                    $("#screensize-submit").attr("disabled", "disabled");
                    $("#screensize-submit").val("Saving...");
                },
                success: function(response) {
                    console.log(response)
                    if (response.status) {                        
                        // $(".carousel__button").click()
                        // FilterCountry('')
                        $(".msg_desc").text(response.message)
                        $("#flash_message_success").attr("style", "display:block;")
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;")
                        }, 3500)
                        location.reload(true);
                        form.trigger('reset');
                        form.trigger('.data-bs-dismiss');
                    } else {
                        // alert('ho')
                    console.log(response.message)
                        if ('message' in response ){
                            // $(".carousel__button").click()
                            $(".msg_desc").text(response.message)
                            $("#flash_message_error").attr("style", "display:block;")
                            setTimeout(function() {
                                $("#flash_message_error").attr("style", "display:none;")
                            }, 3500) 
                                                                                 
                        } else {     
                            alert('form')                    
                            $('#screensize-form-div').html(response.template)     
                        } 
                    }                
                },
                complete: function() {
                    $("#screensize-submit").attr("disabled", false);
                    $("#screensize-submit").val("Save");
                },
            });
        },
    });
});


$(document).on('click', '#create_screensize', function(event) {
    event.preventDefault();
    // var url = $(this).attr('data-url')
    $.ajax({
        url: '/screensize/create/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#screensize-form-div').html('Loading...')
        },
        success: function(response) { 
            console.log(response)
            // console.log(response.template)
            $('#screensize-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });

})


$(document).on('click', '.screensize-edit', function(event) {
    event.preventDefault();
    // const id = document.getElementById('screensize-edit').getAttribute('data-screensize-id');
    var id = $(this).data('screensize-id');
    
    var url = '/screensize/' + String(id) + '/update/'
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: {},
        beforeSend: function() {
            $('#screensize-form-div').html('Loading...')
        },
        success: function(response) {
            console.log(response)
            $('#screensize-form-div').html(response.template)
            $('#popup_head').html(response.title)
        },
    });
})

function FilterScreensizes(page) {
    if (page == '') {
        page = $('#current_page').val()
    }
    var url = $('#load_screensize').val()
    $.ajax({
        url: url,
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        method: "GET",
        data: { 'page': page },
        beforeSend: function() {},
        success: function(response) {
            $('#screensize-tbody').html(response.template)
            $('#screensize-pagination').html(response.pagination)
        },
    });
}

function DeleteScreensize(id) {
    console.log(id)
    var url = '/screensize/' + String(id) + '/delete/'
    swal({
        icon: "warning",
        title: "Verify Details",
        text: "Are you sure you want to delete this record?",
        buttons: true,
        dangerMode: true,
    }).then(function(okey) {
        if (okey) {
            $.ajax({
                url: url,
                headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                method: "POST",
                data: {},
                beforeSend: function() {},
                success: function(response) {
                    console.log(response.message)
                    if (response.status) {
                        $(".msg_desc").text(response.message);
                        $("#flash_message_success").attr("style", "display:block;");
                        setTimeout(function() {
                            $("#flash_message_success").attr("style", "display:none;");
                        }, 3500);
                        // FilterCountry('')
                        location.reload(true);

                    }
                },
            });
        }
    });
}


// $(document).ready(function(){
//     $('.switch')
// })
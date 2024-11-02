$(function(){
    $('div').on({ 'click':()=>{ $('div').css('background-color','red');
            $('div').text('click');
        },
        'dblclick':()=>{
            $('div').css('background-color','green');
            $('div').text('dbclick');

        },
        'mouseenter':()=>{
            $('div').css('background-color','blue');
            $('div').text('mouseenter');

        },
        'mouseout':()=>{
            $('div').css('background-color','gray');
            $('div').text('mouseout');
        },
    })
})
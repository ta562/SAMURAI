from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

def index_view(request):
    #モデルBlogPostのオブジェクトにorder_by()を適用して投稿日時の降順で並び変える
    records = BlogPost.objects.order_by('-posted_at')
    paginator = Paginator(records,4)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    #1引数HTTPrequestオブジェクト2引数レンダリングするテンプレート３引数テンプレートに引き渡すdictデータ
    return render(
        request, 'index.html', {'orderby_records': pages})

def blog_detail(request,pk):
    record=BlogPost.objects.get(id=pk)
    return render(
        request,'post.html',{'object': record})

def science_view(request):
    records = BlogPost.objects.filter(category='science').order_by('-posted_at')
    paginator = Paginator(records,2)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(
        request,'science_list.html', {'orderby_records': pages})

def dailylife_view(request):
    records=BlogPost.objects.filter(category='dailylife'
                                    ).order_by('-posted_at')
    paginator = Paginator(records,2)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(
        request,'dailylife_list.html', {'orderby_records': pages})

def music_view(request):
    records = BlogPost.objects.filter(category='music').order_by('-posted_at')
    paginator = Paginator(records,2)
    page_number = request.GET.get('page',1)
    pages = paginator.page(page_number)
    return render(
        request,'music_list.html',{'orderby_records':pages})

def contact_view(request):
    if request.method == 'GET':
        form=ContactForm()
        return render(request,"contact.html",{'form':form})
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            title=form.cleaned_data['title']
            message=form.cleaned_data['message']
            subject='お問い合わせ:{}'.format(title)
                     
            message=\
                '送信者:{0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'\
                .format(name, email, title, message)
            from_email='admin@example.com'
            to_list=['admin@example.com']
            message=EmailMessage(subject=subject,
                                          body=message,
                                          from_email=from_email,
                                          to=to_list,
                                          )
            message.send()
            messages.success(request,'お問い合わせは正常に')
            return redirect('blogapp:contact')
        
class IndexView(ListView):
    template_name='index.html'
    context_object_name='orderby_records'
    queryset=BlogPost.objects.order_by('-posted_at')
    paginate_by = 2
 
class BlogDetail(DetailView):
    #詳細ページのビュー
        #port.htmlをレンダリングする
    template_name='post.html'
        #クラス変数にmodelにBlohPostを設定
    model=BlogPost

class ScienceView(ListView):
    template_name='science_list.html'
    model=BlogPost
    context_object_name='science_records'
    queryset=BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    paginate_by=2
    
class DailylifeView(ListView):
    template_name='dailylife_list.html'
    model=BlogPost
    context_object_name='dailylife_records'
    queryset=BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    paginate_by=2
    
class MusicView(ListView):
    template_name='music_list.html'
    model=BlogPost
    context_object_name='music_records'
    queryset=BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    paginate_by=2
    
class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    srccess_url=reverse_lazy('blogapp:contact')
    def form_valid(self,form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message ='送信者: {0}\nメールアドレス: {1}\nタイトル:\n{2}\nメッセージ:\n{3}'.format(name,email,title,message)
        from_email='tomo092777tomo@gmail.com'
        to_list=['tomo092777tomo@gmail.com']
        message=EmailMessage(subject=subject,
                             body=message,from_email=from_email,
                             to=to_list,)
        message.send()
        messages.success(self.request,'お問い合わせは正常に送信されました')
        return super().form_valid(form)        
    
Blog Post CRUD System:

- Post Model: title, content, published_date, author
- ListView: /posts/ → shows all posts
- DetailView: /posts/<pk>/ → shows full post
- CreateView: /posts/new/ → only logged-in users
- UpdateView: /posts/<pk>/edit/ → only author
- DeleteView: /posts/<pk>/delete/ → only author
- Permissions enforced via LoginRequiredMixin & UserPassesTestMixin
- Templates: post_list.html, post_detail.html, post_form.html, post_confirm_delete.html
- Forms: PostForm (title + content; author set automatically)
- CSRF protection included in all forms

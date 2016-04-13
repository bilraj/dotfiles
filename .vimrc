execute pathogen#infect()

set number
set relativenumber
set exrc
set secure
:au FocusLost * : set number
:au FocusGained * : set relativenumber
autocmd InsertEnter * : set number
autocmd InsertLeave * : set relativenumber 
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab

set colorcolumn=80
highlight ColorColumn ctermbg=red

autocmd bufenter * if (winnr("$") == 1 && exists ("b:NERDTree") && b:NERDTree.isTabTree()) | q| endif

function! NumberToggle()
  if(&relativenumber == 1)
	 set number
  else
     set relative number
  endif
endfunc

nnoremap <C-n> :call NumberToggle<cr>


syntax enable
set background=dark
colorscheme railscasts 

set backspace=indent,eol,start

set autoindent
set cindent
imap <C-Return> <CR><CR><C-o>k<Tab>

"Set cursor settings so it looks different on Insert mode
highlight Cursor guifg=white guibg=black
highlight iCursor guifg=white guibg=steelblue
set guicursor=n-v-c:block-Cursor
set guicursor+=i:ver100-iCursor
set guicursor+=n-v-c:blinkon0
set guicursor+=i:blinkwait180

"Set leader key
let mapleader=","

"Enable filetype plugin for comments
"filetype plugin on 

"Enable map r to delete without yanking
vmap r "_dP"

"Enable function folding
"set foldmethod=syntax
"let c_no_comment_fold = 1

" Set highlighting on
:set hls
nnoremap <CR> :noh<CR><CR>

" Set split window navigation with ctrl-j
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Tell vim to remember certain things when we exit
"  '10  :  marks will be remembered for up to 10 previously edited files
"  "100 :  will save up to 100 lines for each register
"  :20  :  up to 20 lines of command-line history will be remembered
"  %    :  saves and restores the buffer list
"  n... :  where to save the viminfo files
set viminfo='10,\"100,:20,%,n~/.viminfo

" Set cursor on last edit
function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction

augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END

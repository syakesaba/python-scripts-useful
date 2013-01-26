"  thanks krisleech

:set nocompatible

" ---------------------------------------------------------------------------
" General
" ---------------------------------------------------------------------------

:filetype plugin indent on
:let mapleader = ","
:let g:mapleader = ","
:set modelines=0
:set history=1000
:set nobackup
:set nowritebackup
:set noswapfile
:syntax enable
:set autoread


" ---------------------------------------------------------------------------
" UI
" ---------------------------------------------------------------------------

:set notitle
:set encoding=utf-8
:set scrolloff=3
:set autoindent
:set smartindent
:set showmode
:set showmatch
:set showcmd
:set hidden
:set wildmenu
:set wildmode=list:longest
:set visualbell
:set cursorline
:set ttyfast
:set ruler
:set backspace=indent,eol,start
:set laststatus=2
:set number
":set relativenumber
":set undofile
" "Auto adjust window sizes when they become current
"set winwidth=84
"set winheight=5
"set winminheight=5
"set winheight=999
"colorscheme solarized
"set background=light " or dark
"set t_Co=256"
:set splitbelow splitright

" ---------------------------------------------------------------------------
" Text Formatting
" ---------------------------------------------------------------------------

:set tabstop=4
:set shiftwidth=4
:set softtabstop=4
:set smarttab 
:set expandtab
:set nowrap
:set textwidth=79
:set formatoptions=n
"PEP 8 compatible

" check to make sure vim has been compiled with colorcolumn support
" before enabling it
:if exists("+colorcolumn")
  :set colorcolumn=80
:endif

if has("syntax")
 :syntax on
endif
:set laststatus=2
:set list
":set listchars=eol:¬
:set listchars=eol:¬,tab:>\ 
:set incsearch
:set hlsearch
:set cindent
:set number
:set ruler
:set whichwrap=b,s,h,l,<,>,[,]
:set nowrapscan
:autocmd FileType c,cpp,perl,python,ruby,perl,bash,csh,sh set cindent
:autocmd FileType c set omnifunc=ccomplete#Complete
:set complete+=k
:set backspace=indent,eol,start
:set wildmenu
:set paste
:set nobackup
:set expandtab
:set smartcase
:set ignorecase
"Status line
":set statusline +=%1*\ %n\ %*            "buffer number
:set statusline +=%2*%{&ff}%*            "file format
:set statusline +=%3*%y%*                "file type
:set statusline +=%4*\ %<%F%*            "file name
:set statusline +=%5*%=%m%*                "modified flag
:set statusline +=%6*%5l%*             "current line
:set statusline +=%7*/%L%*               "total lines
:set statusline +=%8*%4v\ %*             "virtual column number
":hi User1 guifg=red guibg=blue ctermfg=red ctermbg=blue
:hi User2 guifg=red guibg=blue ctermfg=white ctermbg=blue
:hi User3 guifg=red guibg=blue ctermfg=white ctermbg=blue
:hi User4 guifg=red guibg=blue ctermfg=white ctermbg=blue
:hi User5 guifg=red guibg=blue ctermfg=white ctermbg=blue
:hi User6 guifg=red guibg=blue ctermfg=white ctermbg=blue
:hi User7 guifg=red guibg=blue ctermfg=white ctermbg=blue
:hi User8 guifg=red guibg=blue ctermfg=white ctermbg=blue
" Colour
":hi StatusLine ctermfg=Black ctermbg=White

" Change colour of statusline in insert mode
":au InsertEnter hi statusline ctermbg=DarkBlue
":au InsertLeave hi statusline ctermfg=Black ctermbg=White

##########
# params #
##########
# debug the makefile?
DO_MKDBG?=0
# do toots?
DO_TOOLS:=1
# do you want dependency on the Makefile itself ?
DO_ALLDEP:=1

########
# code #
########
ALL:=
OUT:=out
TOOLS:=$(OUT)/tools.stamp

ifeq ($(DO_MKDBG),1)
Q=
# we are not silent in this branch
else # DO_MKDBG
Q=@
#.SILENT:
endif # DO_MKDBG

ifeq ($(DO_TOOLS),1)
ALL+=$(TOOLS)
endif # DO_TOOLS

# dependency on the makefile itself
ifeq ($(DO_ALLDEP),1)
.EXTRA_PREREQS+=$(foreach mk, ${MAKEFILE_LIST},$(abspath ${mk}))
endif # DO_ALLDEP

#########
# rules #
#########
# do not add a body for this rule
.PHONY: all
all: $(ALL)
	@true
.PHONY: debug
debug:
	$(info ALL is $(ALL))
$(TOOLS): packages.txt config/deps.py
	$(info doing [$@])
	$(Q)pymakehelper touch_mkdir $@
.PHONY: clean_hard
clean_hard:
	@git clean -qffxd
.PHONY: clean
clean:
	@rm $(TOOLS)

include /usr/share/templar/make/Makefile
##########
# params #
##########
# debug the makefile?
DO_MKDBG?=0
# do doots?
DO_TOOLS:=1
# should we depend on the date of the makefile itself ?
DO_MAKEDEPS:=1

########
# code #
########
ALL:=
OUT:=out
ALL_DEP:=Makefile
TOOLS_STAMP:=$(OUT)/tools.stamp

ifeq ($(DO_MKDBG),1)
Q=
# we are not silent in this branch
else # DO_MKDBG
Q=@
#.SILENT:
endif # DO_MKDBG

ifeq ($(DO_TOOLS),1)
ALL+=$(TOOLS_STAMP)
endif # DO_TOOLS

ALL_DEP:=
ifeq ($(DO_MAKEDEPS),1)
ALL_DEP:=$(ALL_DEP) Makefile
endif # DO_MAKEDEPS

#########
# rules #
#########
# do not add a body for this rule
.PHONY: all
all: $(ALL) $(ALL_DEP)

.PHONY: debug_me
debug_me:
	$(info ALL is $(ALL))

$(TOOLS_STAMP): templardefs/deps.py $(ALL_DEP)
	$(info doing [$@])
	$(Q)templar_cmd install_deps
	$(Q)make_helper touch-mkdir $@

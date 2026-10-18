// Uni-Schedule Dev Diary Entries
// To add an entry: copy-paste an object block at the TOP of the array.
// Any tag you put in the "tags" array will AUTOMATICALLY generate a filter button in the UI!

const ENTRIES = [
  {
    "date": "2026-10-18",
    "title": "Implemented automated README sync",
    "status": "feature",
    "badge": "Auto-Sync",
    "tags": [
      "automation",
      "devlog"
    ],
    "open": true,
    "target": "devlog/sync_readme.py",
    "bullets": [
      "Auto syncs top 3 entries to README",
      "Removes oldest entry automatically"
    ],
    "terminal": ""
  },


  {
    "date": "2026-10-18",
    "title": "Verified Supabase database connection and RLS policies",
    "status": "passed",
    "badge": "RLS Verified",
    "tags": [
      "database",
      "supabase",
      "backend"
    ],
    "open": true,
    "target": "backend/app/db/supabase.py",
    "bullets": [
      "Created mock client",
      "Tested row-level security policies"
    ],
    "terminal": ""
  },

  {
    date: "2026-10-18",
    title: "Passed Schedule CRUD collision edge-cases",
    status: "passed", // 'passed' | 'wip' | 'refactor' | 'bugfix' | 'feature'
    badge: "14/14 Passed ✅",
    tags: ["tests", "backend", "schedule"],
    open: true, // true = unfolded by default, false = folded
    target: "backend/testing/v1/unit/services/schedule/test_schedule_CRUD.py",
    bullets: [
      "Added test coverage for overlapping timeslot requests across semester bounds.",
      "Verified classroom capacity limits properly reject overbooking with HTTP 409.",
      "Ensured schedule entity relations serialize cleanly."
    ],
    terminal: "pytest backend/testing/v1/unit/services/schedule/ -v\n# 14 passed in 0.42s"
  },
  {
    date: "2026-10-17",
    title: "JWT Logout & token blacklisting unit tests verified",
    status: "passed",
    badge: "8/8 Passed ✅",
    tags: ["tests", "auth", "backend"],
    open: false,
    target: "backend/testing/v1/unit/services/user_auth/test_user_login_out.py",
    bullets: [
      "Verified that revoked tokens cannot access protected schedule routes.",
      "Simulated refresh token rotation and replay attack mitigation."
    ],
    terminal: "pytest backend/testing/v1/unit/services/user_auth/test_user_login_out.py\n# 8 passed in 0.28s"
  },
  {
    date: "2026-10-15",
    title: "Separated Group CRUD service from Schedule router",
    status: "refactor",
    badge: "Refactored",
    tags: ["backend", "refactor"],
    open: false,
    target: "backend/app/services/v1/group_CRUD.py",
    bullets: [
      "Decoupled group assignment logic to prevent circular imports in v1 routers.",
      "Prepared data contracts for multi-student batch scheduling."
    ],
    terminal: ""
  }
];
